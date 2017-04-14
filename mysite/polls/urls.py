from django.conf.urls import url

from . import views

#allows server to find url on which to run app
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]