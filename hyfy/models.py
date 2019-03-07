from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=36, unique=True)
    # slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
    #    self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'cities'  #may be Cities

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=36, unique=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'genres'  #may be Cities

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

#class Venue(models.Model):
#   name = models.CharField(max_length=36, unique=True)
#    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#    city = models.ForeignKey(Genre, on_delete=models.CASCADE)
#    likes = models.IntegerField(default=0)


#    def __str__(self):
#        return self.name




