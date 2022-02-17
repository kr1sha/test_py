from django.urls import path

from .views import my_profile_views

app_name = 'profiles'


urlpatterns = [
    path('', my_profile_views, name='main')
]
