from django.contrib import admin
from .models import *


class Film_ImageInline(admin.TabularInline):
    model=Film_Image
    extra = 0

class Film_GenreAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Film_Genre._meta.fields]
    class Meta:
        model=Film_Genre

admin.site.register(Film_Genre, Film_GenreAdmin)

class FilmAdmin(admin.ModelAdmin):

    
    list_display = [field.name for field in Film._meta.fields]
    inlines = [Film_ImageInline]
    class Meta:
        model=Film


admin.site.register(Film, FilmAdmin)

class Film_ImageAdmin(admin.ModelAdmin):

    
    list_display = [field.name for field in Film_Image._meta.fields]
    
    class Meta:
        model=Film_Image


admin.site.register(Film_Image, Film_ImageAdmin)

