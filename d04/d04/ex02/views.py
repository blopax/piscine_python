import os
from django.shortcuts import render
from . import forms
from django.utils import timezone
from django.conf import settings


def form_to_log(request, form):
    if not os.path.exists(os.path.dirname(settings.HISTORY_PATH)):
        os.makedirs(os.path.dirname(settings.HISTORY_PATH))
    if form.is_valid():
        with open(settings.HISTORY_PATH, 'a+') as fd:
            fd.write("{} {}\n".format(timezone.localtime().strftime("%Y-%m-%d %H:%M:%S"), request.POST['text_field']))


def history_treatment():
    if os.path.exists(settings.HISTORY_PATH):
        with open(settings.HISTORY_PATH, 'r+') as fd:
            return fd.read().split('\n')[:-1]


def form(request):
    if request.method == "POST":
        form = forms.FormHistory(request.POST)
        form_to_log(request, form)
    history = history_treatment()
    form = forms.FormHistory()

    return render(request, 'ex02/index.html', {'form': form, 'history': history})
