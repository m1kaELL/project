from django.shortcuts import render
from .forms import SubscriberForm
from films.models import Film_Image

def index(request):

    form=SubscriberForm(request.POST or None)
   
    if request.method=="POST" and form.is_valid():
        print(form)
        
        new_form=form.save()
    form=SubscriberForm()

    return render(request,"Subscribers/index.html",{"form": form})

def home (request):

    films_images = Film_Image.objects.filter(is_active = True,is_main = True, film__is_active=True)
    films_images_fear = films_images.filter(film__genre__id = 2)
    films_images_comedy = films_images.filter(film__genre__id = 1)
    
    return render(request,"Subscribers/home.html", locals())

def film_list (request):

    films_images = Film_Image.objects.filter(is_active = True, film__is_active=True)
    #films_images_fear = films_images.filter(film__genre__id = 2)
    #films_images_comedy = films_images.filter(film__genre__id = 1)
    
    return render(request,"film_list/film_list.html", locals())