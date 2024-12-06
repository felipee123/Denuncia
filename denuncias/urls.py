from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anonymous-report/', views.anonymous_report, name='anonymous_report'),
    path('non-anonymous-report/', views.non_anonymous_report, name='non_anonymous_report'),
    path('search-report/', views.search_report, name='search_report'),
]
