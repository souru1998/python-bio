from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('port',views.innerpage),
    path('contactform/',views.contactform),
    path('login/',views.login),
    path('register/',views.register),

    path('cv/',views.contactview),
    path('updatedC/',views.updatecontact),
    path('delete/',views.deletecontact),

    path('registration/',views.registrationform),
    path('log/',views.loginform),

    path('logout/',views.logout),

]