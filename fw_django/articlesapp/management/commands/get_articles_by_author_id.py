from django.core.management.base import BaseCommand

from articlesapp.models import AuthorModel, ArticleModel


class Command(BaseCommand):
    help = "Get all articles by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = AuthorModel.objects.filter(pk=pk).first()
        if author is not None:
            articles = ArticleModel.objects.filter(author=author)
            intro = f'All articles of {author.fullname}\n'
            text = '\n'.join(article.get_summary() for article in articles)
            self.stdout.write(f'{intro}{text}')
