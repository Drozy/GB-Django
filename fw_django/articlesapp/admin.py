from django.contrib import admin

from .models import AuthorModel, ArticleModel, CommentModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'dob']
    search_fields = ['fullname']
    search_help_text = "Search by author's name"
    exclude = ['fullname']


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'publication_flag']
    ordering = ['category', 'author']
    list_filter = ['category', 'author', 'publication_flag']
    search_fields = ['title']
    search_help_text = 'Search article by title'
    readonly_fields = ['publication_date', 'views_count']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title', 'author', 'category'],
            },
        ),
        (
            'Content',
            {
                'classes': ['collapse'],
                'fields': ['content'],
            },
        ),
        (
            'Publication information',
            {
                'fields': ['publication_flag', 'publication_date', 'views_count'],
            }
        ),
    ]


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'author', 'text', 'changed_date']
    ordering = ['article', 'author', 'changed_date']
    list_filter = ['article', 'author']
    readonly_fields = ['publication_date', 'changed_date']
