from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import datetime
from django.utils.timezone import now
import os


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=36, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'cities'  #may be Cities

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=36, unique=False)
    genrename = models.CharField(max_length=36)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genrename)
        super(Genre, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'genres'  

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=36, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre_venue_set')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_venue_set')
    likes = models.IntegerField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    address = models.TextField(max_length=200, blank=True)
    website = models.URLField(max_length=500,blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Venue, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'venues' 

    def __str__(self):
        return self.name

# class review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    bio = models.TextField(max_length=500,blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    spotifyPicture = models.URLField(max_length=500, default="placeholder")
    spotifyDisplayName = models.TextField(max_length=100, default="placeholder")
    spotifyLink = models.URLField(max_length=500 , default="placeholder")
    topGenre = models.CharField(max_length = 50, default = "placeholder")
    artist0link = models.URLField(max_length=500, default="placeholder")
    artist0imglink = models.URLField(max_length=500, default="placeholder")
    artist1link = models.URLField(max_length=500, default="placeholder")
    artist1imglink = models.URLField(max_length=500, default="placeholder")
    artist2link = models.URLField(max_length=500, default="placeholder")
    artist2imglink = models.URLField(max_length=500, default="placeholder")
    artist3link = models.URLField(max_length=500, default="placeholder")
    artist3imglink = models.URLField(max_length=500, default="placeholder")
    artist4link = models.URLField(max_length=500, default="placeholder")
    artist4imglink = models.URLField(max_length=500, default="placeholder")
    artist5link = models.URLField(max_length=500, default="placeholder")
    artist5imglink = models.URLField(max_length=500, default="placeholder")
    artist6link = models.URLField(max_length=500, default="placeholder")
    artist6imglink = models.URLField(max_length=500, default="placeholder")
    artist7link = models.URLField(max_length=500, default="placeholder")
    artist7imglink = models.URLField(max_length=500, default="placeholder")
    artist8link = models.URLField(max_length=500, default="placeholder")
    artist8imglink = models.URLField(max_length=500, default="placeholder")
    

    # Override the __unicode__() method to return out something meaningful!

    def __str__(self):
        return self.user.username

class Review(models.Model):
    venue = models.ForeignKey(Venue)
    username = models.CharField(User, max_length=100)
    date = datetime.date.today()
    # date = models.DateField(default=now, blank=True, editable=True) #<<< might work (Ollie)
    text = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'reviews' 

    def __str__(self):
        return self.text

class Contact(models.Model):
    user = models.CharField(User, max_length=100)
    date = datetime.date.today()
    # date = models.DateField(default=now, blank=True, editable=True) #<<< might work (Ollie)
    text = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.text

# user = models.OneToOneField(User, on_delete=models.CASCADE)
# bio = models.TextField(max_length=500, blank=True)
# location = models.CharField(max_length=30, blank=True)
# birth_date = models.DateField(null=True, blank=True)
# picture = models.ImageField(upload_to='profile_images', blank=True)

# class SpotifyProfile(models.Model):
#     spotifyUser = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     displayName = models.CharField(max_length=100, blank=True)
#     spotifyURL = models.URLField(max_length=150, blank=True)
#     #topArtists = SeparatedValuesField() #should we make artists an entity
#     topGenres = SeparatedValuesField()
    
