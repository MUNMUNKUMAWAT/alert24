
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls, name="admin"),
        path('', views.home, name = 'home'),
        path('india/', views.india, name='india'),
        path('bollywood/', views.bollywood, name='bollywood'),
        path('sports/', views.sports, name='sports'),
        path('health/', views.health, name='health'),
        path('contact/', views.contact, name='contact'),
        path('entertainment/', views.entertainment, name='entertainment'),
        path('political/', views.political, name='political'),
        path('AllNews/', views.allnews, name='AllNews'),
        path('details/<int:id>', views.details, name='details'),
        path('form/', views.studentsview),
        path('search/', views.search, name="search")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

