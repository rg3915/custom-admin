from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, GroupRequiredMixin


def home(request):
    return render(request, 'index.html')


class LoggedView(LoginRequiredMixin, TemplateView):
    template_name = 'core/logged.html'


class DirectorTemplateView(GroupRequiredMixin, TemplateView):
    template_name = 'core/director.html'
    group_required = u'Diretor'
