from django.db import models

class Style(models.Model):
    style_name = models.CharField(max_length=200)
    style_image = models.ImageField(null=True, blank=True, upload_to='images')
    tasting_note = models.CharField(max_length=200)

    def __str__(self):
        return self.style_name

