from django.urls import path,include
from . import views
urlpatterns = [
    path('master3',views.master3Fn,name='master3'),
    path('booking',views.bookFn,name='booking'),
    path('finished',views.finishFn,name='finished'),
    path('profedit',views.editFn,name='profedit'),
    path('profcrt',views.createFn,name='profcrt'),
    path('eventdash',views.evedashFn,name='eventdash'),
    path('eventpay',views.evepayFn,name='eventpay'),
    path('eventreview',views.evereviewFn,name='eventreview'),
    path('eventview',views.eveviewFn,name='eventview')
]