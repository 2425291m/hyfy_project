import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hyfy_project.settings')

import django
django.setup()
from hyfy.models import City, Genre

def populate():

    glasgow_genres = [
        {"name": "rock"},
        {"name": "pop"},
        {"name": "dance"},
        {"name": "jazz"} ]

    edinburgh_genres = [
        {"name": "rock1"},
        {"name": "pop1"},
        {"name": "dance1"},
        {"name": "jazz1"} ]

    dundee_genres = [
        {"name": "rock2"},
        {"name": "pop2"},
        {"name": "dance2"},
        {"name": "jazz2"} ]
    
    cities = {"Glasgow": {"genres": glasgow_genres},
        "Edinburgh": {"genres": edinburgh_genres},
        "Dundee": {"genres": dundee_genres} }
    
    for city, city_data in cities.items():
        c = add_city(city)
        for g in city_data["genres"]:
            add_genre(g["name"],c)

def add_genre(name, city):
    g = Genre.objects.get_or_create(name=name, city=city)[0]
    g.save()
    return g

def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Hyfy population script...")
    populate()
