from django.urls import path

from . import views

app_name = 'myitem'


urlpatterns = [
    path('', views.index, name='index'),
]
