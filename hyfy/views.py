from django.shortcuts import render
from django.shortcuts import redirect
from hyfy.forms import UserForm, UserProfileForm
from hyfy.forms import ReviewForm, ContactForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from hyfy.models import UserProfile
from hyfy.models import City
from hyfy.models import Venue
from hyfy.models import Genre
from hyfy.models import Review
from django.core.mail import send_mail
from registration.backends.simple.views import RegistrationView
from django.db.models import Q 
import os
import datetime

# Create your views here.

def index(request):
    city_list = City.objects.all
    context_dict = {'cities': city_list}

    response = render(request, 'hyfy/HomePage.html', context_dict)
    return response


def about_us(request):

    response = render(request, 'hyfy/about_us.html')
    return response

def faq(request):

    response = render(request, 'hyfy/faq.html')
    return response

def show_venues_by_genre(request, city_name_slug, genre_name_slug):

    context_dict = {}
    try:
        cities = City.objects.all
        city = City.objects.get(slug=city_name_slug)
        genre = Genre.objects.get(city=city, slug=genre_name_slug)
       
        all_venues = Venue.objects.filter(city=city)

        top_venues = all_venues.filter(genre=genre)

        context_dict['top_venues'] = top_venues
        context_dict['cities'] = cities
        context_dict['city'] = city
        context_dict['genre'] = genre
    except City.DoesNotExist:
        context_dict['city'] = None
        context_dict['genre'] = None

    return render(request,'hyfy/venues_by_genre.html', context=context_dict)

def show_city(request, city_name_slug):

    context_dict = {}

    try:
        cities = City.objects.all
        city = City.objects.get(slug=city_name_slug)
        genres = Genre.objects.filter(city=city)
        all_venues = Venue.objects.filter(city=city)
        rock = genres.filter(genrename="ROCK")
        pop = genres.filter(genrename="POP")
        dance = genres.filter(genrename="DANCE")
        jazz = genres.filter(genrename="JAZZ")

        ordered_rock = all_venues.filter(genre=rock).order_by('-likes')
        ordered_pop = all_venues.filter(genre=pop).order_by('-likes')
        ordered_dance = all_venues.filter(genre=dance).order_by('-likes')
        ordered_jazz = all_venues.filter(genre=jazz).order_by('-likes')
        
        top_rock = ordered_rock.first()
        top_pop = ordered_pop.first()
        top_dance = ordered_dance.first()
        top_jazz = ordered_jazz.first()

        top_venues = {top_rock, top_pop, top_dance, top_jazz}

        context_dict['top_venues'] = top_venues
        context_dict['city'] = city
        context_dict['genres'] = genres
        context_dict['cities'] = cities
    except City.DoesNotExist:
        context_dict['city'] = None
        context_dict['top_venues'] = None
        context_dict['genres'] = None

    return render(request,'hyfy/city.html', context=context_dict)

def like_venue(request, city_name_slug, venue_name_slug):

    venue = Venue.objects.get(slug=venue_name_slug)
    venue.likes = venue.likes+1
    venue.save()

    return show_venue(request, city_name_slug, venue_name_slug)


def show_venue(request, city_name_slug, venue_name_slug):

    context_dict = {}
    try:
        venue = Venue.objects.get(slug=venue_name_slug)
        reviews = Review.objects.all().filter(venue=venue).order_by('-id')[:5]
        context_dict['venue'] = venue
        context_dict['reviews'] = reviews

    except City.DoesNotExist:
        context_dict['venue'] = None

    return render(request,'hyfy/venue.html', context=context_dict)

def user_login(request):
    response = render(request, 'hyfy/login.html')
    return response

def user_details(request):

    if request.method == 'POST':
        username = request.POST.get('id','')
        display_name = request.POST.get('displayname','')
        spotify_link = request.POST.get('spotifylink','')
        spotify_img = request.POST.get('spotifyphoto','')
        topGenre = request.POST.get('topGenre')
        a0link = request.POST.get('artist0link','')
        a0img = request.POST.get('artist0img','')
        a1link = request.POST.get('artist1link','')
        a1img = request.POST.get('artist1img','')
        a2link = request.POST.get('artist2link','')
        a2img = request.POST.get('artist2img','')
        a3link = request.POST.get('artist3link','')
        a3img = request.POST.get('artist3img','')
        a4link = request.POST.get('artist4link','')
        a4img = request.POST.get('artist4img','')
        a5link = request.POST.get('artist5link','')
        a5img = request.POST.get('artist5img','')
        a6link = request.POST.get('artist6link','')
        a6img = request.POST.get('artist6img','')
        a7link = request.POST.get('artist7link','')
        a7img = request.POST.get('artist7img','')
        a8link = request.POST.get('artist8link','')
        a8img = request.POST.get('artist8img','')
        print(username)
        print(display_name)
        print(spotify_link)
        print(spotify_img)
        print(a0link)
        print(a0img)
        print("...")
        print(a8link)
        print(a8img)
        user = User.objects.get(username=username)
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        print(userprofile)
        print(userprofile.spotifyLink)
        userprofile.spotifyDisplayName = display_name
        userprofile.spotifyLink = spotify_link
        userprofile.spotifyPicture = spotify_img
        userprofile.topGenre = topGenre
        userprofile.artist0imglink = a0img
        userprofile.artist0link = a0link
        userprofile.artist1imglink = a1img
        userprofile.artist1link = a1link
        userprofile.artist2imglink = a2img
        userprofile.artist2link = a2link
        userprofile.artist3imglink = a3img
        userprofile.artist3link = a3link
        userprofile.artist4imglink = a4img
        userprofile.artist4link = a4link
        userprofile.artist5imglink = a5img
        userprofile.artist5link = a5link
        userprofile.artist6imglink = a6img
        userprofile.artist6link = a6link
        userprofile.artist7imglink = a7img
        userprofile.artist7link = a7link
        userprofile.artist8imglink = a8img
        userprofile.artist8link = a8link

        
        userprofile.save()

        return render(request, 'hyfy/account.html')

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'hyfy/login.html', {})

def add_review(request):

    if request.method == 'POST':
        venue_slug = request.POST.get('venue_slug', '')
        venue = Venue.objects.get(slug=venue_slug)
        comment_text = request.POST.get('comment', '')

        new_review = Review()
        new_review.venue = venue
        new_review.username = request.user.username
        new_review.date = datetime.date.today()
        new_review.text = comment_text

        new_review.save()
    
    reviews = Review.objects.all().filter(venue=venue)
    return render(request, 'hyfy/show_review.html', context={'reviews': reviews})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_username = form.cleaned_data['username']
            try:
                user = User.objects.get(username = sender_username)
                message = "Account'" + user.username +"' has sent you a new message:\n\n{1}".format(user.username, form.cleaned_data['message'])
                send_mail('New Enquiry', message, user.username, ['euan_M108@hotmail.com'])
                return HttpResponseRedirect(reverse('index'))
            except User.DoesNotExist:
                return HttpResponse("Invalid account name")
    else:
        form = ContactForm()

    return render(request, 'hyfy/contact_us.html', {'form': form})



def thanks(request):
    response = render(request, 'hyfy/thanks.html')
    return response
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def account(request, username):
    try:
        user = User.objects.get(username=username)
        reviews = Review.objects.all().filter(username=username).order_by('-id')[:5]
    except User.DoesNotExist:
        return redirect('index')
    
    #userprofile = UserProfile.objects.get_or_create(user=user)[0]
    userprofile = UserProfile.objects.get(user=user)
    print(userprofile)
    print(userprofile.artist0link)


   # print(userprofile.a0link)
    form = UserProfileForm({'bio': userprofile.bio, 'picture': userprofile.picture})
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'hyfy/account.html', {'userprof': userprofile, 'selecteduser': user, 'form': form, 'picture': userprofile.spotifyPicture, 'reviews': reviews})


def search(request):
    template = 'hyfy/venue_list.html'
    city_list = City.objects.all
    queryName = request.GET.get('q')
    query = request.GET.get('q')
    results = Venue.objects.filter(Q(name__icontains=query))

    context = {'venues': results, 'cities': city_list}

    return render(request, template, context)


