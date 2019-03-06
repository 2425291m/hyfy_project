from django.contrib import admin
from hyfy.models import City, Genre
# from hyfy.models import Venue

# Register your models here.
class CityAdmin (admin.ModelAdmin):
    list_display = ('name',)

class GenreAdmin (admin.ModelAdmin):
    list_display = ('name',)

# class VenueAdmin (admin.ModelAdmin):
#    list_display('name', 'likes', 'genre', 'city')

admin.site.register(City, CityAdmin)
admin.site.register(Genre, GenreAdmin)
# admin.site.register(Venue, VenueAdmin)