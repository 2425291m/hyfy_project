from django.contrib import admin
from hyfy.models import City

# Register your models here.
class CityAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(City, CityAdmin)