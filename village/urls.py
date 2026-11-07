from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('histoire/', views.histoire, name='histoire'),
    path('patrimoine/', views.patrimoine, name='patrimoine'),
    path('culture/', views.culture, name='culture'),
    path('galerie/', views.galerie, name='galerie'),
    path('contact/', views.contact, name='contact'),
]