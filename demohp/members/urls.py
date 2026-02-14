from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('allmembers/', views.allmembers, name='allmembers'),
    path('allmembers/details/<int:id>', views.details, name='details'),
    path('allmembers/<str:name>', views.namedetails, name='name'),
    path('', views.main, name='main'),

]