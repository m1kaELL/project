from django.urls import path,include
from . import views

urlpatterns = [
    path('123', views.index ,name = "index"),
    path('', views.home ,name = "home"),
    path('list', views.film_list ,name = "home"),

]