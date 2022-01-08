from django.urls import path,include
from . import views
urlpatterns =[
    path('master',views.Masterfn,name='master'),
    path('home',views.HomeFn,name='home'),
    path('home2',views.Home2Fn,name='home2'),
    path('home3',views.Home3Fn,name='home3')
]