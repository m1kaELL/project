from django.shortcuts import render
from films.models import*
from film_list.models import*

def film(request,film_id):

    film=Film.objects.get(id=film_id)

    

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    
    return render(request,'films/film.html',locals())
