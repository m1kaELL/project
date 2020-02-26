from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return " User %s %s" %(self.email,self.name,)

    class Meta:
        verbose_name="Subscriber"
        verbose_name_plural="Subscribers"