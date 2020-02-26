from django import forms
from .models import *

class MyReviewsForm(forms.Form):
    name= forms.CharField(required=True)
    email= forms.CharField(required=True)
    