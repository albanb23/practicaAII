from django.contrib import admin
from django.urls import path

from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index.html/', views.index),
    path('populate/', views.populate),
    path('mostrar_album/', views.mostrar_album),
    path('album_mas_vendido/', views.album_mas_vendido),
    path('album_preorder/', views.album_preorder),
    path('buscar_por_titulo/', views.buscar_por_titulo),
    path('buscar_por_fecha/', views.buscar_por_fecha),
]
