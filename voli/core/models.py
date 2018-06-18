from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50, default='')
    origin_url = models.CharField(max_length=255,unique=True)
    tags = models.ManyToManyField(Tag,related_name='recipes')
    saved_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-saved_at"]






class FilterByTag(forms.Form):
    pass

