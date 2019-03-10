from django.shortcuts import render
from hyfy.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from hyfy.models import City
from hyfy.models import Venue
from hyfy.models import Genre
# Create your views here.


def index(request):
    city_list = City.objects.all
    context_dict = {'cities': city_list}

    response = render(request, 'hyfy/HomePage.html', context_dict)
    return response

def account(request):

    response = render(request, 'hyfy/account.html')
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

def show_city(request, city_name_slug):

    context_dict = {}

    try:
        city = City.objects.get(slug=city_name_slug)
        # venues = Venue.obects. get top venues
        genres = Genre.objects.filter(city=city)
        # venue_list = Venue.objects.filter(genre=genres)
        # venue_list = venue_list.order_by('-likes')[:1]
        venues = Venue.objects.filter(city=city)
        rock = genres.filter(genrename="rock")
        pop = genres.filter(genrename="pop")
        dance = genres.filter(genrename="dance")
        jazz = genres.filter(genrename="jazz")

        top_rock = venues.filter(genre=rock).order_by('-likes')[:1]
        top_pop = venues.filter(genre=pop).order_by('-likes')[:1]
        top_dance = venues.filter(genre=dance).order_by('-likes')[:1]
        top_jazz = venues.filter(genre=jazz).order_by('-likes')[:1]
        
        rock = top_rock.values('name')
        pop = top_pop.values('name')
        dance = top_dance.values('name')
        jazz = top_jazz.values('name')
        top_venues = {rock, pop, dance, jazz}
        print(rock)
        print(pop)
        print(dance)
        print(jazz)
        context_dict['venues'] = venues
        context_dict['city'] = city
        context_dict['genres'] = genres
        context_dict['top_venues'] = top_venues

    except City.DoesNotExist:
        context_dict['city'] = None
        context_dict['venues'] = None
        context_dict['genres'] = None

    return render(request,'hyfy/city.html', context=context_dict)

def venue(request):
    response = render(request, 'hyfy/venue.html')
    return response

def show_venue(request):

    response = render(request, 'hyfy/venue.html')
    return response

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


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))