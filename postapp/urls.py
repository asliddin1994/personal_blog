
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPosts, name='post_all'),
    path('detail/<int:pk>/', views.getPost, name='post_detail'),
    path('filter/<str:tagName>/', views.getPostsByTag, name='post_filter'),
    path('about/', views.about, name='about_me')
]
