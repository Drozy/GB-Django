"""
Задание №3
📌 Создайте модель Автор. Модель должна содержать следующие поля:
○ имя до 100 символов
○ фамилия до 100 символов
○ почта
○ биография
○ день рождения
📌 Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

Задание №4
📌 Создайте модель Статья (публикация). Авторы из прошлой задачи могут
писать статьи. У статьи может быть только один автор. У статьи должны быть
следующие обязательные поля:
○ заголовок статьи с максимальной длиной 200 символов
○ содержание статьи
○ дата публикации статьи
○ автор статьи с удалением связанных объектов при удалении автора
○ категория статьи с максимальной длиной 100 символов
○ количество просмотров статьи со значением по умолчанию 0
○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

Задание №6
📌 Создайте модель Комментарий.
📌 Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор.
📌 И комментарий относится к одной статье. У модели должны быть следующие поля
○ автор
○ статья
○ комментарий
○ дата создания
○ дата изменения
"""
from django.db import models
from django.urls import reverse


class AuthorModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    dob = models.DateField()
    fullname = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.fullname = self.firstname + ' ' + self.lastname
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Name: {self.fullname}, email: {self.email}'


class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(AuthorModel, related_name='author_article_set', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    publication_flag = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('article_full', kwargs={'article_id': self.pk})

    def __str__(self):
        return f'{self.title}'

    def get_summary(self):
        words = str(self.content).split()
        return f'{" ".join(words[:12])}...'


class CommentModel(models.Model):
    author = models.ForeignKey(AuthorModel, related_name='author_comment_set', on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, related_name='article_comment_set', on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    changed_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.publication_date}: {self.text}'
