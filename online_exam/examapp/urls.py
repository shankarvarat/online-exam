
from django.urls import path
from .views import *
urlpatterns = [
    path('index', index),
    path('profile',profile,name='profile'),
    path('',loginu,name='loginu' ),
    path('loginu', loginu, name='loginu'),

    path('signup', signup,name='signup'),
    path('logoutu',logoutu,name='logoutu'),
    path('texam', texam,name='texam'),

]
