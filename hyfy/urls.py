# urls.py /hyfy

from django.conf.urls import url, include
from hyfy import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^user_details/$',views.user_details, name='user_details'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^like_venue/(?P<city_name_slug>[\w\-]+)/(?P<venue_name_slug>[\w\-]+)$', views.like_venue, name='like_venue'),
    
    # url(r'^show_review/(?P<venue_name_slug>[\w\-]+)/$', views.show_review, name='show_review'),
    
    # url(r'^submitted/$', views.submitted, name='submitted'),
    # url(r'^show_review/(?P<username>[\w\-]+)/(?P<venue_name_slug>[\w\-]+)/$', views.show_review, name='show_review'),
    url(r'^(?P<city_name_slug>[\w\-]+)/$', views.show_city, name='show_city'),
    url(r'^account/(?P<username>[\w\-]+)/$', views.account, name='account'),
    # url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    # url(r'^venue/$', views.venue, name='venue'),
    url(r'^(?P<city_name_slug>[\w\-]+)/(?P<venue_name_slug>[\w\-]+)/$', views.show_venue, name='show_venue'),
    url(r'^venues_by_genre/(?P<city_name_slug>[\w\-]+)/(?P<genre_name_slug>[\w\-]+)/$', views.show_venues_by_genre, name='show_venues_by_genre'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

    #    path('social/', include('social_django.urls')),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    # url(r'^add_category/$', views.add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    #

    # url(r'^register/$', views.register, name='register'),  # New pattern!
]
