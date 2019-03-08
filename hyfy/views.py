from django.shortcuts import render
from hyfy.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def index(request):

    response = render(request, 'hyfy/HomePage.html')
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

def show_top_venues(request, city_name_slug):

    context_dict = {}
    
    return render(request,'hyfy/top_venues.html',context_dict)

def venue(request):
    response = render(request, 'hyfy/venue.html')
    return response
    
def show_venue(request):

    response = render(request, 'hyfy/venue.html')
    return response

def top_venues(request):

    response = render(request, 'hyfy/top_venues.html')
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
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))