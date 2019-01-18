from django.views.generic.edit import CreateView
from .models import Files
from django.urls import reverse_lazy
from django.conf import settings


class Home(CreateView):
    model = Files
    fields = ['title', 'upload']
    template_name = 'ex00/home.html'
    success_url = reverse_lazy('home')

    def get_context_data(self):
        context = super(Home, self).get_context_data()
        context['files'] = Files.objects.all()
        context['debug'] = settings.DEBUG
        return context


