from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
urlpatterns = [
    path('', PostListView.as_view(), name="practice-home"),
    path('about/', views.about, name="practice-about"),
    path('post/<int:pk>', PostDetailView.as_view(), name="practice-detail"),
    path('post/new', PostCreateView.as_view(), name="practice-create"), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="practice-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="practice-delete"),
]