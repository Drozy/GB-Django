from django.shortcuts import render, get_object_or_404

from articlesapp.models import AuthorModel, ArticleModel


def author_posts(request, author_id):
    author = get_object_or_404(AuthorModel, pk=author_id)
    articles = ArticleModel.objects.filter(author=author).order_by('id')
    return render(request, 'articlesapp/author_articles.html',
                  {'author': author, 'articles': articles})


def article_full(request, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views_count += 1
    article.save()
    return render(request, 'articlesapp/article.html', {'article': article})
