from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path('autor/', views.blog_autor, name="blog_autor"),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('article/', views.article, name='article'),
    path('subscription/', views.subscription, name='subscription'),
    path('search/', views.get_blog_queryset, name='search'),
    path('tag/', views.tagged, name='tag'),
]