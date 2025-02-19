from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('1_1', views.target1, name='1_1'),
    path('1_2', views.actual1, name='1_2'),
    path('2_1', views.class2, name='2_1'),
    path('2_2', views.risk2, name='2_2'),
    path('3_1', views.tech3, name='3_1'),
    path('3_2', views.org3, name='3_2'),
    path('4_1', views.regular4, name='4_1'),
    path('4_2', views.incident4, name='4_2'),
    path('5_1', views.rez5, name='5_1'),
    path('5_2', views.grow5, name='5_2'),
    path('templ', views.templ, name='templ'),
    path('cheme', views.cheme, name='cheme'),
    path('termin', views.termin, name='termin'),

]
