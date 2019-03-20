import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hyfy_project.settings')

import django
django.setup()
from hyfy.models import City, Genre, Venue


def populate():


    glarock_venues = [
        {"name": "Oran Mor", "likes": 10, "lat": 55.8776, "long": 4.2898, "address": "Top of Byres Road, Glasgow, G12 8QX", "website": "https://oran-mor.co.uk/"},
        {"name": "Broadcast", "likes": 2, "lat": 55.8660, "long": 4.2691, "address": "427 Sauchiehall Street, Glasgow G2 3LG", "website": "https://broadcastglasgow.com/"},
        {"name": "O2 ABC Glasgow", "likes": 4, "lat": 55.8656, "long": 4.2642, "address": "300 Sauchiehall Street, Glasgow G2 3JA", "website": "https://www.academymusicgroup.com/o2abcglasgow/"},
    ]

    glapop_venues = [
        {"name": "The Blue Arrow", "likes": 3, "lat": 55.8616, "long": 4.2586, "address": "323 Sauchiehall Street, Glasgow G2 3HW", "website": "https://www.thebluearrow.co.uk/"},
        {"name": "O2 Academy Glasgow", "likes": 15, "lat": 55.8506, "long": 4.2595, "address": "121 Eglinton Street, Glasgow G5 9NT", "website": "https://www.academymusicgroup.com/o2academyglasgow/"},
        {"name": "SSE Hydro", "likes": 8, "lat": 55.8602, "long": 44.2853, "address": "Exhibition Way, Glasgow G3 8YW", "website": "https://www.thessehydro.com/"},
    ]

    gladance_venues = [
        {"name": "The Garage", "likes": 40, "lat": 55.8661, "long": 4.2685, "address": "490 Sauchiehall Street, Glasgow,G2 3LW", "website": "https://garageglasgow.co.uk/"},
        {"name": "The Sanctuary", "likes": 15, "lat": 55.8698, "long": 4.2966, "address": "59 Dumbarton Road, Glasgow G11 6PD", "website": "https://www.thesanctuaryglasgow.com/"},
        {"name": "The Viper", "likes": 5, "lat": 55.8757, "long": 4.2823, "address": "500 Great Western Road, Glasgow G12 8EN", "website": "https://www.viperwestend.co.uk/"},
    ]

    glajazz_venues = [
        {"name": "Swing", "likes": 9, "lat": 55.8630, "long": 4.2581, "address": "183 Hope Street, Glasgow G2 2UL", "website": "https://swingltd.co.uk/"},
        {"name": "Dukes Bar", "likes": 18, "lat": 55.8670, "long": 4.2922, "address": "41 Old Dumbarton Road, Glasgow G3 8RD", "website": "http://www.dukes-bar.co.uk/"},
        {"name": "Three Judges", "likes": 3, "lat": 55.8703, "long": 4.2994, "address": "141 Dumbarton Rd, Glasgow G11 6PR", "website": "https://www.greatukpubs.co.uk/threejudges"},
    ]

    edirock_venues = [
        {"name": "Electric Circus", "likes": 20, "lat": 55.9512, "long": 3.1900, "address": "36-39 Market Street, Edinburgh EH1 1DF", "website": "https://www.theelectriccircus.biz/"},
        {"name": "Bannerman's Bar", "likes": 1, "lat": 55.9488, "long": 3.1866, "address": "212 Cowgate, Edinburgh EH1 1NQ", "website": "https://www.bannermanslive.co.uk/"},
        {"name": "The Bongo House", "likes": 10, "lat": 55.9482, "long": 3.1922, "address": "66 Cowgate, Edinburgh EH1 1JX", "website": "http://www.thebongoclub.co.uk/"},
    ]

    edipop_venues = [
        {"name": "The Queen's Hall", "likes": 4, "lat": 55.9412, "long": 3.1816, "address": "The Queen's Hall, Clerk Street, Edinburgh EH8 9JG", "website": "https://www.thequeenshall.net/"},
        {"name": "Stramash Live Music Bar", "likes": 17, "lat": 55.9486, "long": 3.1878, "address": "207 Cowgate, Edinburgh EH1 1JQ", "website": "https://stramashedinburgh.com/"},
        {"name": "La Belle Angele", "likes": 5, "lat": 55.9485, "long": 3.1875, "address": "11 Hastie's Close, Edinburgh EH1 1HJ", "website": "https://la-belleangele.com/"},
    ]

    edidance_venues = [
        {"name": "Cabaret Voltaire", "likes": 2, "lat": 55.9489, "long": 3.1873, "address": "36-38 Blair Street, Edinburgh EH1 1QR", "website": "http://www.thecabaretvoltaire.com/"},
        {"name": "The Liquid Room", "likes": 4, "lat": 55.9486, "long": 3.1938, "address": "9C Victoria St, Edinburgh EH1 2HE", "website": "http://www.liquidroom.com/"},
        {"name": "Hive", "likes": 60, "lat": 55.9496, "long": 3.1870, "address": "15-17 Niddry Street, Edinburgh EH1 1LG", "website": "https://www.facebook.com/clubhive"},
    ]

    edijazz_venues = [
        {"name": "The Jazz Bar", "likes": 2, "lat": 55.9481, "long": 3.1870, "address": "A, 1 Chambers Street, Edinburgh EH1 1HR", "website": "http://www.thejazzbar.co.uk/"},
        {"name": "Dirty Martini", "likes": 8, "lat": 55.9534, "long": 3.1960, "address": "16 George Street, Edinburgh EH2 2PF", "website": "https://lemondehotel.co.uk/drink/dirty-martini/"},
        {"name": "Voodoo Rooms", "likes": 6, "lat": 55.9538, "long": 3.1906, "address": "19a W Register Street, Edinburgh EH2 2AA", "website": "http://www.thevoodoorooms.com/"},
    ]

    dunrock_venues = [
        {"name": "Conroy's Basement", "likes": 5, "lat": 56.4636, "long": 2.9703, "address": "51-53 Meadowside, Dundee DD1 1EQ", "website": "https://www.facebook.com/conroysbasement/"},
        {"name": "Church", "likes": 4, "lat": 56.4617, "long": 2.9758, "address": "15 Ward Road, Dundee DD1 1ND", "website": "https://www.musicglue.com/churchdundee"},
    ]

    dunpop_venues = [
        {"name": "Dundee University SU", "likes": 10, "lat": 56.4578, "long": 2.9822, "address": "Airlie Place, Dundee DD1 4HP", "website": "https://www.dusa.co.uk/"},
        {"name": "Fat Sams", "likes": 30, "lat": 56.4608, "long": 2.9770, "address": "31 S Ward Road, Dundee DD1 1PU", "website": "https://www.fatsams.co.uk/"},
    ]

    dundance_venues = [
        {"name": "Beat Generator Live!", "likes": 9, "lat": 56.4608, "long": 2.9761, "address": "70 N Lindsay Street, Dundee DD1 1PS", "website": "http://www.beatgenerator.co.uk/"},
        {"name": "Club Tropicana", "likes": 2, "lat": 56.4606, "long": 2.9771, "address": "31 S Ward Road, Dundee DD1 1PU", "website": "https://www.facebook.com/TropicanaDundee/"},
    ]

    dunjazz_venues = [
        {"name": "Gardyne Theatre", "likes": 16, "lat": 56.4721, "long": 2.9113, "address": "Gardyne Campus, Gardyne Road, Dundee DD5 1NY", "website": "http://www.gardynetheatre.org.uk/"},
        {"name": "Clarks", "likes": 2, "lat": 56.4611, "long": 2.9766, "address": "80 N Lindsay Street, Dundee DD1 1PS", "website": "https://www.clarksonlindsaystreet.com/"},
    ]

    genres = {"Glasgow_rock": {"venues": glarock_venues},
            "Glasgow_pop": {"venues": glapop_venues},
            "Glasgow_jazz": {"venues": glajazz_venues},
            "Glasgow_dance": {"venues": glajazz_venues}}

    glasgow_genres = [
        {"name": "gla_rock", "genrename": "ROCK", "venues": glarock_venues},
        {"name": "gla_pop", "genrename": "POP", "venues": glapop_venues},
        {"name": "gla_dance", "genrename": "DANCE", "venues": gladance_venues},
        {"name": "gla_jazz", "genrename": "JAZZ", "venues": glajazz_venues}]

    edinburgh_genres = [
        {"name": "edi_rock", "genrename": "ROCK", "venues": edirock_venues},
        {"name": "edi_pop", "genrename": "POP", "venues": edipop_venues},
        {"name": "edi_dance", "genrename": "DANCE", "venues": edidance_venues},
        {"name": "edi_jazz", "genrename": "JAZZ", "venues": edijazz_venues}]

    dundee_genres = [
        {"name": "dun_rock", "genrename": "ROCK", "venues": dunrock_venues},
        {"name": "dun_pop", "genrename": "POP", "venues": dunpop_venues},
        {"name": "dun_dance", "genrename": "DANCE", "venues": dundance_venues},
        {"name": "dun_jazz", "genrename": "JAZZ", "venues": dunjazz_venues}]

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
                print(v["address"])
                add_venue(v["name"], thisgenre, thiscity,
                        v["likes"], v["long"], v["lat"], v["address"], v["website"])


def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_genre(name, genrename, city):
    g = Genre.objects.get_or_create(name=name, city=city)[0]
    g.genrename = genrename
    g.save()
    return g

def add_venue(name, genre, city, likes, longitude, latitude, address, website):
    v = Venue.objects.get_or_create(name=name, genre=genre, city=city)[0]
    v.likes=likes
    v.longitude=longitude
    v.latitude=latitude
    v.address=address
    v.website=website
    v.save()
    return v



# Start execution here!
if __name__ == '__main__':
    print("Starting Hyfy population script...")
    populate()
