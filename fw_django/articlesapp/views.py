from django.shortcuts import render, get_object_or_404, redirect

from articlesapp.forms import AuthorForm, ArticleForm, CommentForm
from articlesapp.models import AuthorModel, ArticleModel, CommentModel

form_create = 'articlesapp/form_create.html'


def author_posts(request, author_id):
    author = get_object_or_404(AuthorModel, pk=author_id)
    articles = ArticleModel.objects.filter(author=author).order_by('id')
    return render(request, 'articlesapp/author_articles.html',
                  {'author': author, 'articles': articles})


def article_full(request, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views_count += 1
    article.save()
    comments = CommentModel.objects.filter(article=article).order_by('-changed_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CommentModel.objects.create(
                author=data['author'],
                article=article,
                text=data['text'],
            )
            return redirect(article_full, article_id)
    return render(request, 'articlesapp/article.html',
                  {'article': article, 'form': CommentForm(), 'comments': comments})


def create_author(request):
    title = 'Create new author'
    message = ''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            # data = form.cleaned_data
            # AuthorModel.objects.create(
            #     firstname=data['firstname'],
            #     lastname=data['lastname'],
            #     email=data['email'],
            #     bio=data['bio'],
            #     dob=data['dob'],
            # )
            message = 'New author added'
        else:
            render(request, form_create, {'title': title, 'form': form})
    return render(request, form_create, {'title': title, 'form': AuthorForm(), 'message': message})


def create_post(request):
    title = 'Create new article'
    message = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'New article added'
        else:
            render(request, form_create, {'title': title, 'form': form})
    return render(request, form_create, {'title': title, 'form': ArticleForm(), 'message': message})
