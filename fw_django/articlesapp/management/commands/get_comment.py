from django.core.management.base import BaseCommand
from articlesapp.models import CommentModel


class Command(BaseCommand):
    help = "Get comment by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Comment ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        comment = CommentModel.objects.filter(pk=pk).first()
        self.stdout.write(f'{comment}')
