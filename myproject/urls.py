from django.conf.urls import url
from django.contrib import admin
from myproject.core import views as c

urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
