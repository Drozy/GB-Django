from django.urls import path
from . import views

urlpatterns = [
    path('author_posts/<int:author_id>', views.author_posts, name='author_posts'),
    path('article/<int:article_id>', views.article_full, name='article_full'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_post/', views.create_post, name='create_post'),
]
