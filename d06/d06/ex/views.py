from django.shortcuts import render, redirect
from d06 import settings
import random
from ex.models import TipUser, Tip, Upvotes, Downvotes
from ex.forms import SignUpForm, SignInForm, TipForm
from django.contrib.auth import authenticate, login, models
from django.contrib.auth.models import Permission


def anonymous_session(request, url, context):
    index = request.COOKIES.get('index', None)
    context['connected'] = None
    if not index:
        index = random.randint(0, 9)
        context['username'] = settings.NAMES[index]
        response = render(request, 'ex/home.html', context)
        response.set_cookie('index', index, max_age=settings.SESSION_COOKIE_AGE)
    else:
        context['username'] = settings.NAMES[int(index)]
        response = render(request, url, context)
    return response


def add_tip(request):
    form = TipForm(request.POST)
    if form.is_valid():
        author = request.COOKIES.get('username')
        content = form.cleaned_data['content']
        t = Tip(content=content, author=author)
        t.save()


def upvote(username, t):
    try:
        if username not in t.upvotes.all().values_list('vote_user', flat=True):
            print("bob", t.upvotes.all())
            t.upvotes.create(vote_user=str(username))
            print("bob")
            if username in t.downvotes.all().values_list('vote_user', flat=True):
                t.downvotes.get(vote_user=username).delete()
        else:
            t.upvotes.get(vote_user=username).delete()
    except Tip.DoesNotExist as err:
        pass


def downvote(username, t):
    try:
        if username not in t.downvotes.all().values_list('vote_user', flat=True):
            t.downvotes.create(vote_user=username)
            if username in t.upvotes.all().values_list('vote_user', flat=True):
                t.upvotes.get(vote_user=username).delete()
        else:
            t.downvotes.get(vote_user=username).delete()
    except Tip.DoesNotExist as err:
        print(err)


def remove_tip(t, username):
    try:
        if t.author == username or TipUser.objects.get(username=username).has_perm('ex.delete_tip'):
            t.delete()
    except Tip.DoesNotExist as err:
        print(err)


def home(request):
    u = TipUser.objects.all()
    print(u)
    connected = request.COOKIES.get('connected', None)
    if not connected:
        return anonymous_session(request, 'ex/home.html', {})
    username = request.COOKIES.get('username', None)
    if request.method == "POST":
        if 'add_tip' in request.POST:
            add_tip(request)
        if 'upvote' in request.POST:
            t = Tip.objects.get(id=request.POST['upvote'])
            upvote(username, t)
        if 'downvote' in request.POST:
            t = Tip.objects.get(id=request.POST['downvote'])
            downvote(username, t)
        if 'remove' in request.POST:
            t = Tip.objects.get(id=request.POST['remove'])
            remove_tip(t, username)
    form = TipForm()
    tips = Tip.objects.all()
    for tip in tips:
        tip.upvotes_count = len(tip.upvotes.all())
        tip.downvotes_count = len(tip.downvotes.all())
    return render(request, 'ex/home.html', {'username': username, 'connected': connected, 'form': form, 'tips': tips})


def sign_in(request):
    connected = request.COOKIES.get('connected', None)
    if connected:
        return redirect('/')
    if request.method != 'POST':
        form = SignInForm()
        return anonymous_session(request, 'ex/authentification.html', {'form': form})

    form = SignInForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        username = authenticate(username=username, password=password)
        if username:
            login(request, username)
            response = redirect('/')
            response.set_cookie('username', username)
            response.set_cookie('connected', 1)
            return response
        else:
            form._errors['username'] = ["This username doesn't exist or the password is wrong"]
    return render(request, 'ex/authentification.html', {'form': form})


def sign_up(request):
    connected = request.COOKIES.get('connected', None)
    if connected:
        return redirect('/')
    if request.method != 'POST':
        form = SignUpForm()
        return anonymous_session(request, 'ex/authentification.html', {'form': form})
    form = SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        password_verification = form.cleaned_data['password_verification']
        if password == password_verification:
            try:
                u = TipUser(username=username)
                u.set_password(password)
                u.save()
                response = redirect('/')
                response.set_cookie('username', u.username)
                response.set_cookie('connected', 1)
                return response
            except Exception as err:
                form._errors['username'] = ['The username already exists']
        else:
            form._errors['password'] = ["The passwords don't match"]
    return render(request, 'ex/authentification.html', {'form': form})


def log_out(request):
    response = redirect('/')
    response.delete_cookie('username')
    response.delete_cookie('connected')
    return response

