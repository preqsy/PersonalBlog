from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single_post/<str:pk>/', views.single_post, name='single_post'),
    path('single_trend/<str:pk>/', views.single_trend, name='single_trend'),
    path('single_business/<str:pk>/', views.single_business, name='single_business'),
    path('single_culture/<str:pk>/', views.single_culture, name='single_culture'),
    path('single_lifestyle/<str:pk>/', views.single_lifestyle, name='single_lifestyle'),
    path('single_headline/<str:pk>/', views.single_headline, name='single_headline'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('category', views.category, name='category'),
    path('search_result', views.search_result, name='search_result'),

]