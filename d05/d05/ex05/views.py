from django.shortcuts import HttpResponse, render
from .models import Movies


def add_movie(title, episode_nb, director, producer, release_date):
    try:
        m = Movies(title, episode_nb, None, director, producer, release_date)
        m.save()
        print_value = "OK<br/>"
    except Exception as err:
        print_value = "{}<br/>".format(err)
    print(print_value)
    return print_value

def populate(request):
    print_value = add_movie('The Phantom Menace', 1, 'George Lucas', 'Rick McCallum', '1999-05-19')
    print_value += add_movie('Attack of the Clones', 2, 'George Lucas', 'Rick McCallum', '2002-05-16')
    print_value += add_movie('Revenge of the Sith', 3, 'George Lucas', 'Rick McCallum', '2005-05-19')
    print_value += add_movie('A New Hope', 4, 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25')
    print_value += add_movie('The Empire Strikes Back', 5, 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')
    print_value += add_movie('Return of the Jedi', 6, 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum',
              '1983-05-25')
    print_value += add_movie('The Force Awakens', 7, 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    return HttpResponse(print_value)


def display(request):
    try:
        table = Movies.objects.all().order_by('episode_nb')
    except Exception as err:
        table = None
        print(err)

    return render(request, 'ex05/display.html', {'table': table})


def remove(request):
    title = request.POST.get('title', None)
    try:
        if title:
            to_be_removed = Movies.objects.filter(title=title)
            to_be_removed.delete()
        table = Movies.objects.all().order_by('episode_nb')
    except Exception as err:
        table = None

    return render(request, 'ex05/remove.html', {'table': table})

