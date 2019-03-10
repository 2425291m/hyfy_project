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
        {"name": "The Blue Arrow", "likes": 3, "lat": 55.8616, "long": 4.2586, }
    ]

    gladance_venues = [
        {"name": "The Garage", "likes": 100, "lat": 55.8661, "long": 4.2685}
    ]

    glajazz_venues = [
        {"name": "Swing", "likes": 9, "lat": 55.8630, "long": 4.2581}
    ]

    edirock_venues = [
        {"name": "edirockPH", "likes": 10, "lat": 55.8776, "long": 4.2898}
    ]

    edipop_venues = [
        {"name": "edipopPH", "likes": 3, "lat": 55.8616, "long": 4.2586, }
    ]

    edidance_venues = [
        {"name": "edidancePH", "likes": 100, "lat": 55.8661, "long": 4.2685}
    ]

    edijazz_venues = [
        {"name": "edijazzPH", "likes": 9, "lat": 55.8630, "long": 4.2581}
    ]

    dunrock_venues = [
        {"name": "dunrockPH", "likes": 10, "lat": 55.8776, "long": 4.2898}
    ]

    dunpop_venues = [
        {"name": "dunpopPH", "likes": 3, "lat": 55.8616, "long": 4.2586, }
    ]

    dundance_venues = [
        {"name": "dundancePH", "likes": 100, "lat": 55.8661, "long": 4.2685}
    ]

    dunjazz_venues = [
        {"name": "dunjazzPH", "likes": 9, "lat": 55.8630, "long": 4.2581}
    ]

    genres = {"Glasgow_rock": {"venues": glarock_venues},
            "Glasgow_pop": {"venues": glapop_venues},
            "Glasgow_jazz": {"venues": glajazz_venues},
            "Glasgow_dance": {"venues": glajazz_venues}}

    glasgow_genres = [
        {"name": "gla_rock", "genrename": "rock", "venues": glarock_venues},
        {"name": "gla_pop", "genrename": "pop", "venues": glapop_venues},
        {"name": "gla_dance", "genrename": "dance", "venues": gladance_venues},
        {"name": "gla_jazz", "genrename": "jazz", "venues": glajazz_venues}]

    edinburgh_genres = [
        {"name": "edi_rock", "genrename": "rock", "venues": edirock_venues},
        {"name": "edi_pop", "genrename": "pop", "venues": edipop_venues},
        {"name": "edi_dance", "genrename": "dance", "venues": edidance_venues},
        {"name": "edi_jazz", "genrename": "jazz", "venues": edijazz_venues}]

    dundee_genres = [
        {"name": "dun_rock", "genrename": "rock", "venues": dunrock_venues},
        {"name": "dun_pop", "genrename": "pop", "venues": dunpop_venues},
        {"name": "dun_dance", "genrename": "dance", "venues": dundance_venues},
        {"name": "dun_jazz", "genrename": "jazz", "venues": dunjazz_venues}]

    cities = [{"name": "Glasgow", "genres": glasgow_genres},
            {"name": "Edinburgh", "genres": edinburgh_genres},
            {"name": "Dundee", "genres": dundee_genres}]


    for c in cities:
        print(c["name"])
        print(c["genres"])
        thiscity  = add_city(c["name"])
        for g in c["genres"]:
            print(g)
            print("name = " +  g["name"])
            print("genrename = " + g["genrename"])
            print("cityname = " + c["name"])
            thisgenre  = add_genre(g["name"], g["genrename"], thiscity)
            for v in g["venues"]:
                print(v["name"])
                print(g["genrename"])
                print(c["name"])
                print(v["likes"])
                print(v["long"])
                print(v["lat"])
                add_venue(v["name"], thisgenre, thiscity,
                        v["likes"], v["long"], v["lat"])


def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_genre(name, genrename, city):
    g = Genre.objects.get_or_create(name=name, city=city)[0]
    g.genrename = genrename
    g.save()
    return g

def add_venue(name, genre, city, likes, longitude, latitude):
    v = Venue.objects.get_or_create(name=name, genre=genre, city=city)[0]
    v.likes=likes
    v.longitude=longitude
    v.latitude=latitude
    v.save()
    return v



# Start execution here!
if __name__ == '__main__':
    print("Starting Hyfy population script...")
    populate()
