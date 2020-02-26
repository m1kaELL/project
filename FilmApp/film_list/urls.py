from django.urls import path,include
from .import views

urlpatterns = [
    path('review_adding', views.review_adding,name="review_adding"),
    path('reviews', views.my_reviews,name="my_reviews"),
]
