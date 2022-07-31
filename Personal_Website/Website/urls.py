from django.urls import path, include, reverse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect


app_name = 'Website'

urlpatterns = [
    path('',views.HomePage.as_view(),name="HomePage"),
    path('AboutMe',views.AboutMe.as_view(),name='AboutMe'),
    path('ContactMe',views.ContactMe,name='ContactMe'),
    path('success', views.successView, name = 'success'),
    path('Test',views.TestPage.as_view(),name="Test"),
    path('test_js',views.Test_js.as_view(),name="Test_js"),
    path('Portfolio_main',views.Portfolio_main.as_view(),name='Portfolio_main'),
    path('Project1/',views.Project1,name="Project1"),
    path('Project2/',views.Project2,name="Project2"),

]
