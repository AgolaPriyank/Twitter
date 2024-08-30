from django.urls import path
from . import views


urlpatterns = [
    path('', views.twitt_list , name='twitt_list'),
    
    path('create/', views.twitt_create , name='twitt_create'),
    
    path('<int:twitt_id>/edit/', views.twitt_edit , name='twitt_edit'),
    
    path('<int:twitt_id>/delete/', views.twitt_delete , name='twitt_delete'),
    
    path('register/', views.register , name='register'),
    
] 