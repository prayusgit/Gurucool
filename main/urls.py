from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home-view'),
    path('about/', about_view, name='about-view')
]
