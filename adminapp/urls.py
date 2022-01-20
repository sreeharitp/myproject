from django.urls import path,include
from . import views
urlpatterns =[
    path('master2',views.adminFn,name='master2'),
    path('adminevent',views.eventFn,name='adminevent'),
    path('admindash',views.dashFn,name='admindash'),
    path('customer',views.custFn,name='customer'),
    path('adminpay',views.payFn,name='adminpay'),
    path('adminrating',views.rateFn,name='adminrating'),
    path('addteam',views.addFn,name='addteam'),
    path('custview',views.viewFn,name='custview')
]