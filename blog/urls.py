from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   path('', views.PostListView.as_view(), name='post_list'),
    path('post/list/', views.PostListView.as_view(), name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]
