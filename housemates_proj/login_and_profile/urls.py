from django.urls import path
from . import views

urlpatterns = [
    #### Login Routes ####
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    #### Protected Profile Routes ####
    path('profile', views.profile),
    path('profile/create_house', views.create_house),
    path('profile/select_main_house', views.select_main_house),
    #### Protected House Routes ####
    path('profile/main_house/<int:id>', views.main_house),
    path('profile/main_house/<int:id>/add_housemate', views.add_housemate),


]
