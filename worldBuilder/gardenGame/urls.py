from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainPage, name="main"),
    path('profile/', views.profile, name="profile"),
    path('buildingOfTheDay/', views.buildingOfTheDay, name="buildingOfTheDay"),
    path('reportToAdmin/', views.reportToAdmin, name="reportToAdmin"),
    path('privacyPolicy/', views.privacyPolicy, name="privacyPolicy")

]
