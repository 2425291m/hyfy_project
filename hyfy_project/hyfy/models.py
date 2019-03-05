from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=36, unique=True)
    #slug = models.SlugField(unique=True)

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.name)
    #    super(Category, self).save(*args, **kwargs)

    #class Meta:
    #    verbose_name_plural = 'cities'  #may be Cities

    def __str__(self):
        return self.name