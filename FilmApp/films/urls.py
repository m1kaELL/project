from django.urls import path,include
from films import views

urlpatterns = [
    path('<int:film_id>', views.film,name = "film"),
]
