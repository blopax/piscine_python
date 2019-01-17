from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import RedirectView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate

from ex00.models import Article


class ArticlesList(ListView):
    model = Article


class HomeRedirect(RedirectView):
    pattern_name = 'article_list'


class LoginView(FormView):
    template_name = 'ex00/login_form.html'
    form_class = LoginForm
    success_url = '/'



    def post(self, request):
        f = self.form_class(request.POST)
        print("bob")
        print(f)
        for key in f.keys():
            print(key)
        username = f.cleaned_data['username']
        password = f.cleaned_data['password']
        valid = authenticate(username=username, password=password)
        if f.is_valid():
            print("valid")
        else:
            print("bab")
        return render(request, 'ex00/login_form.html', {"form": f})
    #     if f.is_valid():
    #         username = f.cleaned_data['username']
    #         password = f.cleaned_data['password']
    #         valid = authenticate(username=username, password=password)
    #     if valid == False:
    #         return render(request, template_name, {'form': f})

    # def form_valid(self):
    #     f = self.get_form()
    #     username = f.cleaned_data['username']
    #     password = f.cleaned_data['password']
    #     return authenticate(username=username, password=password)

