from django.contrib import admin

from .models import AuthorModel, ArticleModel, CommentModel

# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(ArticleModel)
admin.site.register(CommentModel)
