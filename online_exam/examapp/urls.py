
from django.urls import path
from .views import *
urlpatterns = [
    path('index', index),
    path('profile',profile,name='profile'),
    path('login',login ),
    path('signup', signup),

]
