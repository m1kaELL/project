from .models import *

def getting_review_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    
    films_review=Film_review.objects.filter(session_key=session_key)
    total_review=films_review.count()

    return locals()
