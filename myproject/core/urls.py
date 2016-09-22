from django.conf.urls import url
from myproject.core import views as c


urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^logged/$', c.LoggedView.as_view(), name='logged'),
    url(r'^director/$', c.DirectorTemplateView.as_view(), name='director'),
]
