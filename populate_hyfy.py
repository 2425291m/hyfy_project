import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hyfy_project.settings')

import django
django.setup()
from hyfy.models import City, Venue

def populate():

    glasgow_venues = [
        {"name": "Oran Mor", "likes": 10, "lat": 55.8776, "long": 4.2898, "genre": "rock"},
        {"name": "Broadcast", "likes": 2, "lat": 55.8660, "long": 4.2691, "genre": "rock"},
        {"name": "The Blue Arrow", "likes": 3, "lat": 55.8616, "long": 4.2586, "genre": "pop"},
        {"name": "The Garage", "likes": 100, "lat": 55.8661, "long": 4.2685, "genre": "dance"},
        {"name": "Swing", "likes": 9, "lat": 55.8630, "long": 4.2581, "genre": "jazz"} ]


    edinburgh_venues = [
        {"name": "The Jazz Bar", "likes": 15, "lat": 55.9481, "long": 3.1870, "genre": "jazz"},
        {"name": "Hive", "likes": 200, "lat": 55.9496, "long": 3.1870, "genre": "dance"} ]

    dundee_venues = [
        {"name": "DUSU", "likes": 300, "lat": 56.4578, "long": 2.9822, "genre": "pop"},
        {"name": "Club Tropicana", "likes": 17, "lat": 56.4606, "long": 2.9771, "genre": "dance"} ]
    
    cities = {"Glasgow": {"venues": glasgow_venues},
        "Edinburgh": {"venues": edinburgh_venues},
        "Dundee": {"venues": dundee_venues} }
    
    for city, city_data in cities.items():
        c = add_city(city)
        for v in city_data["venues"]:
            add_venue(v["name"], c, v['likes'], v["lat"], v["long"], v["genre"])
        

#def add_genre(name, genrename, city):
#    g = Genre.objects.get_or_create(name=name, city=city)[0]
#    g.genrename = genrename
#    g.save()
#    return g

def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_venue(name, city, likes, longitude, latitude, genre):
    v = Venue.objects.get_or_create(city=city, name=name)[0]
    v.likes=likes
    v.longitude=longitude
    v.latitude=latitude
    v.genre = genre
    v.save()
    return v

# Start execution here!
if __name__ == '__main__':
    print("Starting Hyfy population script...")
    populate()
