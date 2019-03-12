from django.contrib import admin
from hyfy.models import City, UserProfile
from hyfy.models import Venue
from hyfy.models import Genre
from hyfy.models import Review

# Register your models here.
class CityAdmin (admin.ModelAdmin):
    list_display = ('name',)

class GenreAdmin (admin.ModelAdmin):
   list_display = ('name','genrename',)

class VenueAdmin (admin.ModelAdmin):
    list_display = ('name', 'city', 'likes', 'latitude', 'longitude', 'genre')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']



admin.site.register(City, CityAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(UserProfile)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Review, ReviewAdmin)