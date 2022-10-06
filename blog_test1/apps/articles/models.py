import datetime

from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=150)
    article_text = models.TextField('Содержание')
    article_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.article_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField('Автор', max_length=150)
    comment_text = models.TextField('Комментарий')

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
