from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name = 'home-page'),
    path('about/', Aboutus, name = 'about-page'),
    path('contact/', ContactUs, name = 'contact-page'),
    path('accountant/', Accountant, name = 'accountant-page'),
    path('register/' ,Register, name = 'register-page'),
    path('profile/', ProfilePage, name = 'profile-page'),
    path('reset-password/', ResetPassword, name = 'reset-password'),
]