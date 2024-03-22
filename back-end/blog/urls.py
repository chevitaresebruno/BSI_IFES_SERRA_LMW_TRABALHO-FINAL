from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('aula_um/', views.aula_um, name='aula_um/'),
    path('aula_dois/', views.aula_dois, name='aula_dois/')
]