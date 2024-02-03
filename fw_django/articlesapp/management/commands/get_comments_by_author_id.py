from django.core.management.base import BaseCommand

from articlesapp.models import AuthorModel, CommentModel


class Command(BaseCommand):
    help = "Get all comments by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = AuthorModel.objects.filter(pk=pk).first()
        if author is not None:
            comments = CommentModel.objects.filter(author=author)
            intro = f'All comments of {author.fullname}\n'
            text = '\n'.join(str(comment) for comment in comments)
            self.stdout.write(f'{intro}{text}')
