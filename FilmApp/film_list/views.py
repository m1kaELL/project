from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from .forms import *

from films.models import*
from django.contrib.auth.models import User


def review_adding(request):
    return_dict=dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    film_id = data.get("film_id")
    number = data.get("number")
    is_delete = data.get("is_delete")

    if is_delete=="true":
        Film_review.objects.filter(film_id=film_id).update(is_active=False)
    else:
        new_review,created = Film_review.objects.update_or_create(session_key=session_key,film_id=film_id,is_active=True,defaults={"number":number})
    
    
    #common code for 2 cases
    films_review=Film_review.objects.filter(session_key=session_key,is_active=True)
    total_review=films_review.count()
    return_dict["total_review"]=total_review
    
    return_dict["films"]=list()
    
    for item in films_review: 
        film_dict=dict()
        film_dict["id"]=item.id
        film_dict["name"]=item.film.title
        film_dict["descr"]=item.number

        return_dict["films"].append(film_dict)
        
    return  JsonResponse(return_dict)


def my_reviews(request):
    session_key = request.session.session_key
    films_review=Film_review.objects.filter(session_key=session_key,is_active=True)
    form= MyReviewsForm(request.POST or None)
    
    if request.POST:
        print(request.POST)
        if form.is_valid:
            print("yes")
            data = request.POST
            name= data.get("name",32123)
            email = data["email"]
            user, created = User.objects.get_or_create(username=email,defaults={"first_name": name})

            film_list = Film_list.objects.create(user=user,user_name=name,user_email=email,status_id=1)
            for name, value in data.items() :
                if name.startswith("review_"):
                    review_id = name.split("review_")[1]
                    film= Film_review.objects.get(id=review_id)
                    review_id.film_list-film_list
                    review_id.total_review = value
                    review_id.save(force_update = True)
                   
                    Film_inf.objects.create(film=review_id.film,number=review_film.number,film_list=film_list)
                    print(id)
        else:
            print("no")
    return render (request, "film_list/reviews.html", locals())




