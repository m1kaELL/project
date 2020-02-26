from django.contrib import admin
from .models import *

class Film_Inline(admin.TabularInline):
    model=Film_inf
    extra = 0

class Film_listAdmin(admin.ModelAdmin):

    
    list_display = [field.name for field in Film_list._meta.fields]
    inlines = [Film_Inline]
    class Meta:
        model=Film_list


admin.site.register(Film_list, Film_listAdmin)

class Film_infAdmin(admin.ModelAdmin):

    
    list_display = [field.name for field in Film_inf._meta.fields]
    
    class Meta:
        model=Film_inf


admin.site.register(Film_inf, Film_infAdmin)

class StatusAdmin(admin.ModelAdmin):

    
    list_display = [field.name for field in Status._meta.fields]
    
    class Meta:
        model=Status


admin.site.register(Status, StatusAdmin)

class Film_reviewAdmin(admin.ModelAdmin):

    
    list_display = [field.name for field in Film_review._meta.fields]
    class Meta:
        model=Film_review
    
admin.site.register(Film_review, Film_reviewAdmin)