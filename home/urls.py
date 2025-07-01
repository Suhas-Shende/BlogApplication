from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('search/<str:slug>/', views.searchpost, name='blogpost'),
    path('create/', views.create, name='create'),
    path('<str:slug>/', views.blogpost, name='blogpost'),
    
   
    
]
