
from django.urls import path
from .views import *
urlpatterns = [
    path('index', index),
    path('uprofile',uprofile,name='uprofile'),
    path('',loginu,name='loginu' ),
    path('loginu', loginu, name='loginu'),
    path('eprofile', eprofile, name='eprofile'),

    path('signup', signup,name='signup'),
    path('logoutu',logoutu,name='logoutu'),
    path('texam', texam,name='texam'),
    path('uans', uans, name='uans'),

]
