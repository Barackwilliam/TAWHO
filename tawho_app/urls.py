from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_us, name='about'),
    path('programs/', views.programs, name='programs'),
    path('membership/', views.membership, name='membership'),
    path('donation/', views.donation, name='donation'),
    path('documents/', views.documents, name='documents'),
    path('contact/', views.contact, name='contact'),
    
    # API endpoints
    path('api/programs/', views.program_list_api, name='program_api'),
    path('api/member-stats/', views.member_stats_api, name='member_stats_api'),
    
    # Success pages
    path('membership/success/', lambda request: render(request, 'membership_success.html'), name='membership_success'),
    path('donation/success/', lambda request: render(request, 'donation_success.html'), name='donation_success'),
    path('contact/success/', lambda request: render(request, 'contact_success.html'), name='contact_success'),
]