from django.db import models
from films.models import Film
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=30,blank=True , null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "Статус: %s" % self.status 

    class Meta:
        verbose_name="Status"
        verbose_name_plural="Statuses"


class Film_list(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    film_id=models.ForeignKey(Film,blank=True , null=True, default=None,on_delete=models.DO_NOTHING)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(blank=True , null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "Список фильмов %s % s" %(self.id,self.status.status)

    class Meta:
        verbose_name="Film_list"
        verbose_name_plural="Film_lists"


class Film_inf(models.Model):
    film_list = models.ForeignKey(Film_list,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    film=models.ForeignKey(Film,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "Фильм %s" % self.film.title

    class Meta:
        verbose_name="Film"
        verbose_name_plural="Films"


#    def save(self, *args, **kwargs):
# для переопределения(умножение и подсчет товаров)
      #  super(Film_inf, self).save(*args, **kwargs)
        
def film_inf_post_save(sender,instance,created,**kwargs):
    film_list=instance.film_list
post_save.connect(film_inf_post_save,sender=Film_inf)


class Film_review(models.Model):
    session_key = models.CharField(max_length=128,blank=True , null=True, default=None)
    film=models.ForeignKey(Film,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    film_list=models.ForeignKey(Film_list,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    number = models.TextField(blank=True , null=True, default=None)
    list_name = models.CharField(max_length=30)
    list_email = models.EmailField(blank=True , null=True, default=None)
    list_comments =models.TextField(blank=True , null= True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " %s " %(self.id)

    class Meta:
        verbose_name="Review"
        verbose_name_plural="Reviews"
