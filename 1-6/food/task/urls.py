from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
 path ('', views.index),
 path ('<id>/delete/', views.delete),
 path ('tambah/', views.tambah),
 path ('<id>/update/', views.update),
 path ('<id>/detail/', views.rincian),
 
]