from email.mime import image
from django.db import models

# Create your models here.

class onechibi(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=800)
    bio = models.CharField(max_length=2000)
    verified_chibi = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']