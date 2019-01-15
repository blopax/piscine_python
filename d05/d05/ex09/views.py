from django.shortcuts import HttpResponse, render
from .models import Planets, People
from datetime import datetime


def display(request):
    try:
        table = People.objects.select_related('homeworld').values(
            'name', 'homeworld__name', 'homeworld__climate').filter(
            homeworld__climate__contains='windy').order_by('name')
    except Exception as err:
        table = None
        print(err)
    return render(request, 'ex09/display.html', {'table': table})

