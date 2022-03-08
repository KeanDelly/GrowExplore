from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainPage, name="main"),
    path('profile/', views.profile, name="profile"),
    path('buildingOfTheDay/', views.buildingOfTheDay, name="buildingOfTheDay")
    #path('profile/', views.login_request, name="login"),
    #path('logout/', views.login_request, name="login"),

]
