from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.DRAFT)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='URl')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор')
    body = models.TextField(verbose_name='Содержание')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.DRAFT, verbose_name='Статус публикации')

    objects = models.Manager()
    published = PublishedManager()
    draft = DraftManager()

    class Meta:

        ordering = ['-publish']

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
