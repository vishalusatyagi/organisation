from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # path('Home/',views.home, name='home'),
    path('OrganisationChart/',views.organisationchart, name='organisaionchart'),
    path('Event/',views.events, name='event'),
    path('Gallery/',views.gallery, name='gallery'),
    path('About/',views.about, name='about'),
    path('Contactus/',views.contactus, name='contactus'),
]