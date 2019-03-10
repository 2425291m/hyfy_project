import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hyfy_project.settings')

import django
django.setup()
from hyfy.models import City, Genre, Venue


def populate():


    glarock_venues = [
        {"name": "Oran Mor", "likes": 10, "lat": 55.8776, "long": 4.2898},
        {"name": "Broadcast", "likes": 2, "lat": 55.8660, "long": 4.2691},
        {"name": "O2 ABC Glasgow", "likes": 4, "lat": 55.8656, "long": 4.2642},
    ]

    glapop_venues = [
        {"name": "The Blue Arrow", "likes": 3, "lat": 55.8616, "long": 4.2586},
        {"name": "O2 Academy Glasgow", "likes": 15, "lat": 55.8506, "long": 4.2595},
        {"name": "SSE Hydro", "likes": 8, "lat": 55.8602, "long": 44.2853},
    ]

    gladance_venues = [
        {"name": "The Garage", "likes": 40, "lat": 55.8661, "long": 4.2685},
        {"name": "The Sanctuary", "likes": 15, "lat": 55.8698, "long": 4.2966},
        {"name": "The Viper", "likes": 5, "lat": 55.8757, "long": 4.2823},
    ]

    glajazz_venues = [
        {"name": "Swing", "likes": 9, "lat": 55.8630, "long": 4.2581},
        {"name": "Dukes Bar", "likes": 18, "lat": 55.8670, "long": 4.2922},
        {"name": "Three Judges", "likes": 3, "lat": 55.8703, "long": 4.2994},
    ]

    edirock_venues = [
        {"name": "Electric Circus", "likes": 20, "lat": 55.9512, "long": 3.1900},
        {"name": "Bannerman's Bar", "likes": 1, "lat": 55.9488, "long": 3.1866},
        {"name": "edirockPH", "likes": 10, "lat": 55.8776, "long": 4.2898},
    ]

    edipop_venues = [
        {"name": "The Queen's Hall", "likes": 4, "lat": 55.9412, "long": 3.1816},
        {"name": "Strasmash Live Music Bar", "likes": 17, "lat": 55.9486, "long": 3.1878},
        {"name": "La Belle Angele", "likes": 5, "lat": 55.9485, "long": 3.1875},
    ]

    edidance_venues = [
        {"name": "Cabaret Voltaire", "likes": 2, "lat": 55.9489, "long": 3.1873},
        {"name": "The Liquid Room", "likes": 4, "lat": 55.9486, "long": 3.1938},
        {"name": "Hive", "likes": 60, "lat": 55.9496, "long": 3.1870},
    ]

    edijazz_venues = [
        {"name": "The Jazz Bar", "likes": 2, "lat": 55.9481, "long": 3.1870},
        {"name": "Dirty Martini", "likes": 8, "lat": 55.9534, "long": 3.1960},
        {"name": "Voodoo Rooms", "likes": 6, "lat": 55.9538, "long": 3.1906},
    ]

    dunrock_venues = [
        {"name": "Conroy's Basement", "likes": 5, "lat": 56.4636, "long": 2.9703},
        {"name": "Church", "likes": 4, "lat": 56.4617, "long": 2.9758},
    ]

    dunpop_venues = [
        {"name": "Dundee University SU", "likes": 10, "lat": 56.4578, "long": 2.9822},
        {"name": "Fat Sams", "likes": 30, "lat": 56.4608, "long": 2.9770},
    ]

    dundance_venues = [
        {"name": "Beat Generator Live!", "likes": 9, "lat": 56.4608, "long": 2.9761},
        {"name": "Club Tropicana", "likes": 2, "lat": 56.4606, "long": 2.9771},
    ]

    dunjazz_venues = [
        {"name": "Gardyne Theatre", "likes": 16, "lat": 56.4721, "long": 2.9113},
        {"name": "Clarks", "likes": 2, "lat": 56.4611, "long": 2.9766},
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
