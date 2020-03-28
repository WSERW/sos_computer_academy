from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('course_ad/', views.course_ad, name='course_ad'),
    path('stud/', views.stud, name='stud'),
]