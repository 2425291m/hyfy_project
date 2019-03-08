# urls.py /hyfy

from django.conf.urls import url
from hyfy import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    # url(r'^venue/(?P<venue_name_slug>[\w\-]+)/$', views.show_venue, name='show_venue'),
    url(r'^venue/$', views.venue, name='venue'),
    
    
    url(r'^login/$', views.user_login, name='login'),
    url(r'^account/$', views.account, name='account'),
    url(r'^register/$', views.register, name='register'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^top_venues/$', views.top_venues, name='top_venues'),
    url(r'^(?P<city_name_slug>[\w\-]+)/$', views.show_top_venues, name='show_top_venues'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    # url(r'^add_category/$', views.add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    #

    # url(r'^register/$', views.register, name='register'),  # New pattern!
]
