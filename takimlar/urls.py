from django.urls import path
from . import views

urlpatterns = [
    path('takim_listesi', views.takim_listesi, name='takim_listesi'),
    path('ekle/', views.takim_ekle, name='takim_ekle'),
    path('guncelle/<int:id>/', views.takim_guncelle, name='takim_guncelle'),
    path('sil/<int:id>/', views.takim_sil, name='takim_sil'),
]
