# urls.py /hyfy_project
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from hyfy import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hyfy/', include('hyfy.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
