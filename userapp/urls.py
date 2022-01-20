from django.urls import path,include
from . import views
urlpatterns =[
    path('master1',views.masterFn,name='master1'),
    path('userhome',views.userhomeFn,name='userhome'),
    path('userhome2',views.userhome2Fn,name='userhome2'),
    path('userhome3',views.userhome3Fn,name='userhome3'),
    path('aboutus',views.aboutFn,name='aboutus'),
    path('contactus',views.contactFn,name='contactus')
]