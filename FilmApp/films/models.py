from django.db import models

class Film_Genre(models.Model):
    name = models.CharField(max_length=30,blank=True , null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Жанр: %s " % self.name

    class Meta:
        verbose_name="Жанр"
        verbose_name_plural="Жанры"

class Film(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True , null=True, default=None)
    genre = models.ForeignKey(Film_Genre,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    short_description = models.TextField(blank=True , null=True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Фильм %s" % self.title

    class Meta:
        verbose_name="Film"
        verbose_name_plural="Films"

class Film_Image(models.Model):
    film = models.ForeignKey(Film,blank=True,null=True,default=None,on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='Subscribers/static/media/films_images/',blank=True , null=True, default=None)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "Фильм %s " % self.film

    class Meta:
        verbose_name="Image"
        verbose_name_plural="Images"
