from django.urls import path
from Master import views

urlpatterns = [
    
     path('', views.home, name = 'home'),
     path('createmobiles', views.createmobiles, name = 'createmobiles'),
     path('viewmobiles', views.viewmobiles, name = 'viewmobiles'),
     path('delete/<str:varCode>', views.delete, name = 'delete'),
     path('search', views.search, name = 'search'),
     path('searchoutput', views.searchoutput, name = 'searchoutput'),
]