from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    response = render(request, 'hyfy/HomePage.html')
    return response

def Account(request):

    response = render(request, 'hyfy/Account.html')
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


def show_venue(request):

    response = render(request, 'hyfy/venue.html')
    return response

def user_login(request):

    response = render(request, 'hyfy/login.html')
    return response







