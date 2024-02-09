from django.urls import path
from . import views

urlpatterns = [
    path('author_posts/<int:author_id>', views.author_posts, name='author_posts'),
    path('article/<int:article_id>', views.article_full, name='article_full'),
]
