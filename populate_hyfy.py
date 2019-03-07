import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hyfy_project.settings')

import django
django.setup()
from hyfy.models import City, Genre

def populate():

    glasgow_genres = [
        {"name": "gla_rock", "genrename": "rock"},
        {"name": "gla_pop", "genrename": "pop"},
        {"name": "gla_dance", "genrename": "dance"},
        {"name": "gla_jazz", "genrename": "jazz"} ]

    edinburgh_genres = [
        {"name": "edi_rock", "genrename": "rock"},
        {"name": "edi_pop", "genrename": "pop"},
        {"name": "edi_dance", "genrename": "dance"},
        {"name": "edi_jazz", "genrename": "jazz"} ]

    dundee_genres = [
        {"name": "dun_rock", "genrename": "rock"},
        {"name": "dun_pop", "genrename": "pop"},
        {"name": "dun_dance", "genrename": "dance"},
        {"name": "dun_jazz", "genrename": "jazz"} ]
    
    cities = {"Glasgow": {"genres": glasgow_genres},
        "Edinburgh": {"genres": edinburgh_genres},
        "Dundee": {"genres": dundee_genres} }

    glarock_venues = [
        {"name": "Oran Mor", "likes": 10, "lat": 55.8776, "long": 4.2898},
        {"name": "Broadcast", "likes": 2, "lat": 55.8660, "long": 4.2691},
    ]

    glapop_venues = [
        {"name": "The Blue Arrow", "likes": 3, "lat": 55.8616, "long": 4.2586,}
    ]

    gladance_venues = [
        {"name": "The Garage", "likes": 100, "lat": 55.8661, "long": 4.2685}
    ]

    glajazz_venues = [
        {"name": "Swing", "likes": 9, "lat": 55.8630, "long": 4.2581}
    ]

    city_genres = {"Glasgow_rock": {"genres": glasgow_rock},
        {"Glasgow_pop": {"genres": glasgow_pop},
        {"Glasgow_jazz": {"genres": glasgow_dance},
        {"Glasgow_dance": {"genres": glasgow_jazz} }

    for city, city_data in cities.items():
        c = add_city(city)
        for g in city_data["genres"]:
            add_genre(g["name"], g["genrename"], c)
            
    for city_genre, genre_data in city_genres.items():
       for v in genre_data["venues"]:
           add_venue(v["name"], )
            

def add_genre(name, genrename, city):
    g = Genre.objects.get_or_create(name=name, genrename=genrename, city=city)[0]
    g.save()
    return g

def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_venue(name, genre, city, likes, longitude, latitude):
    v = Genre.objects.get_or_create(name=name, gname=genre, city=city)[0]
    v.likes=likes
    v.longitude=longitude
    v.latitude=latitude
    return v

# Start execution here!
if __name__ == '__main__':
    print("Starting Hyfy population script...")
    populate()
