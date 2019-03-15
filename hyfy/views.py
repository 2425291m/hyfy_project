from django.shortcuts import render
from django.shortcuts import redirect
from hyfy.forms import UserForm, UserProfileForm
from hyfy.forms import ReviewForm
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


def contact_us(request):

    response = render(request, 'hyfy/contact_us.html')
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

        top_rock = all_venues.filter(genre=rock).first()
        top_pop = all_venues.filter(genre=pop).first()
        top_dance = all_venues.filter(genre=dance).first()
        top_jazz = all_venues.filter(genre=jazz).first()
        
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

def venue(request):
    form = ReviewForm()
    response = render(request, 'hyfy/venue.html', context={'form': form})
    return response

def show_venue(request, city_name_slug, venue_name_slug):
    context_dict = {}
    try:
        venue = Venue.objects.get(slug=venue_name_slug)
        reviews = Review.objects.all().filter(venue=venue)
        context_dict['venue'] = venue
        context_dict['reviews'] = reviews
    except City.DoesNotExist:
        context_dict['venue'] = None

    return render(request,'hyfy/venue.html', context=context_dict)

def user_login(request):
    response = render(request, 'hyfy/login.html')
    return response

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else: 
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'hyfy/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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
        new_review.username = request.user
        new_review.date = datetime.date.today()
        new_review.text = comment_text

        new_review.save()
    
    reviews = Review.objects.all().filter(venue=venue)
    return render(request, 'hyfy/show_review.html', context={'reviews': reviews})


    # form = ReviewForm()
    # venue = Venue.objects.get(slug=venue_name_slug)
    # user = User.objects.get(username=username)

    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():

    #         review = form.save(commit=False)
    #         review.venue = venue
    #         review.username = user.username
    #         review.save()
    #         return submitted(request)
    #     else:
    #         print(form.errors)

    # context_dict = {'form':form, 'venue': venue_name_slug}
    # return render(request, 'hyfy/add_review.html', {'form': form})

    

def submitted(request):

    response = render(request, 'hyfy/submitted.html')
    return response

def show_review(request, venue_name_slug):
   
    context_dict = {}
    try:
        venue = Venue.objects.get(slug=venue_name_slug)
        reviews = Review.objects.filter(venue=venue)

        context_dict['reviews'] = reviews

    except Review.DoesNotExist:
        context_dict['reviews'] = None
       
    response = render(request, 'hyfy/show_review.html', context_dict)
    return response


# def show_review(request):

#     try:
#         all_reviews = Review.objects.filer(venue=venue)


#     return render(request, 'show_reviews.html', {'review': review})

#     context_dict{}

#     try:

#         all_venues = Venue.objects.filter(city=city)
#         rock = genres.filter(genrename="rock")
#         pop = genres.filter(genrename="pop")
#         dance = genres.filter(genrename="dance")
#         jazz = genres.filter(genrename="jazz")

#         top_rock = all_venues.filter(genre=rock).first()
#         top_pop = all_venues.filter(genre=pop).first()
#         top_dance = all_venues.filter(genre=dance).first()
#         top_jazz = all_venues.filter(genre=jazz).first()

#         top_venues = {top_rock, top_pop, top_dance, top_jazz}

#         context_dict['top_venues'] = top_venues
#         context_dict['city'] = city
#         context_dict['genres'] = genres

#     venue = get_object_or_404(Venue)
#     user_name = get_object_or_404(User)
#     form = ReviewForm(request.POST)
#     if form.is_valid():
#         rating = form.cleaned_data['rating']
#         comment = form.cleaned_data['comment']
#         review = Review()
#         review.venue = venue
#         review.user_name = user_name
#         review.rating = rating
#         review.comment = comment
#         review.pub_date = datetime.datetime.now()
#         review.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('reviews':, args=(Venue,)))
#     return render(request, 'reviews/ajax_comment.html', {'review': review})


	
def thanks(request):
    response = render(request, 'hyfy/thanks.html')
    return response
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form':form}
    return render(request, 'hyfy/profile_registration.html', context_dict)

class HyfyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

# def account(request):
   
#     response = render(request, 'hyfy/account.html')
#     return response

@login_required
def account(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'bio': userprofile.bio, 'picture': userprofile.picture})
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    
    return render(request, 'hyfy/account.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})


def search(request):
    template = 'hyfy/venue_list.html'
    city_list = City.objects.all
    queryName = request.GET.get('q')
    query = request.GET.get('q')
    results = Venue.objects.filter(Q(name__icontains=query))

    context = {'venues': results, 'cities': city_list}

    return render(request, template, context)