from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from articlesapp.models import ArticleModel, AuthorModel, CommentModel


class Command(BaseCommand):
    help = "Create comment."

    def add_arguments(self, parser):
        parser.add_argument('author_pk', type=int, help='Author ID')
        parser.add_argument('article_pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        author_pk = kwargs.get('author_pk')
        article_pk = kwargs.get('article_pk')
        author = AuthorModel.objects.filter(pk=author_pk).first()
        article = ArticleModel.objects.filter(pk=article_pk).first()
        if author is not None:
            if article is not None:
                comment = CommentModel(author=author, article=article, text=lorem_ipsum.sentence())
                comment.save()
                self.stdout.write(f'{comment}')
            else:
                self.stdout.write(f'Статья с id={author_pk} не найдена.')
        else:
            self.stdout.write(f'Автор с id={author_pk} не найден.')
