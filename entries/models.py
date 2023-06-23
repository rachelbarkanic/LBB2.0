import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User



class Style(models.Model):
    style_name = models.CharField(max_length=200)
    style_image = models.ImageField(null=True, blank=True, upload_to='images/style_images')
    tasting_note = models.CharField(max_length=200)

    def __str__(self):
        return self.style_name
    


class Entry(models.Model):
    title = models.CharField(max_length=200, default='x')
    beer_name = models.CharField(max_length=200)
    brewery_name = models.CharField(max_length=200)
    beer_pic = models.ImageField(null=True, blank=True, upload_to='images/beer_pics')
    rating = models.IntegerField(default=0)
    content = models.TextField()
    view_count = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, default=False)

    beer_style = models.ForeignKey(Style, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content
