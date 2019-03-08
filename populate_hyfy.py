import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hyfy_project.settings')

import django
django.setup()
from hyfy.models import City, Genre, Venue

def populate():

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

    genres = {"Glasgow_rock": {"venues": glarock_venues},
        "Glasgow_pop": {"venues": glapop_venues},
        "Glasgow_jazz": {"venues": glajazz_venues},
        "Glasgow_dance": {"venues": glajazz_venues} }

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
    
    for city, city_data in cities.items():
        c = add_city(city)
        for g, city_data in city_data["genres"]:
            add_genre(g["name"], g["genrename"], c["name"])
            for v in genres.items():
                add_venue(v["name"], g["genrename"], g["city"], v["likes"], v["lat"], v["long"])
        

def add_genre(name, genrename, city):
    g = Genre.objects.get_or_create(name=name, city=city)[0]
    g.genrename = genrename
    g.save()
    return g

def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_venue(name, genre, city, likes, longitude, latitude):
    v = Genre.objects.get_or_create(name=name, genre=genre, city=city)[0]
    v.likes=likes
    v.longitude=longitude
    v.latitude=latitude
    return v

# Start execution here!
if __name__ == '__main__':
    print("Starting Hyfy population script...")
    populate()
