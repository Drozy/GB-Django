from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import choice

from articlesapp.models import AuthorModel, ArticleModel, CommentModel


class Command(BaseCommand):
    help = "Generate fake authors and articles."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of authors and articles for each author.')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        authors = []
        articles = []
        for i in range(1, count + 1):
            author = AuthorModel(firstname=f'Name{i}', lastname=f'Surname{i}', email=f'author{i}@example.com',
                                 bio=lorem_ipsum.paragraph(), dob='1980-02-22')
            authors.append(author)
            author.save()
            for j in range(1, count + 1):
                article = ArticleModel(title=f'Title{j}',
                                       content=f'Text from {author.fullname} # {j}\n{lorem_ipsum.paragraph()}',
                                       author=author, category=f'Category {i}', publication_flag=True)
                articles.append(article)
                article.save()
        for article in articles:
            for i in range(3):
                comment = CommentModel(author=choice(authors), article=article, text=lorem_ipsum.sentence())
                comment.save()
