from django.contrib import admin
from hyfy.models import City, UserProfile
from hyfy.models import Venue
from hyfy.models import Genre
from hyfy.models import Review, Contact

# Register your models here.
class CityAdmin (admin.ModelAdmin):
    list_display = ('name',)

class GenreAdmin (admin.ModelAdmin):
   list_display = ('name','genrename',)

class VenueAdmin (admin.ModelAdmin):
    list_display = ('name', 'city', 'likes', 'latitude', 'longitude', 'genre')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','text','username','venue','date')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'picture', 'spotifypicture','spotifyDisplayName')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')

admin.site.register(City, CityAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(UserProfile)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Contact, ContactAdmin)