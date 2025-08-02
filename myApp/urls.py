from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),## root url
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register')
]
