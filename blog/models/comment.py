from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    name = models.CharField(max_length=80, verbose_name='Заголовок')
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Содержание')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    active = models.BooleanField(verbose_name='Отображение', default=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created']
        indexes = [models.Index(fields=['created']), ]

    def __str__(self):
        return f"Комментарий от {self.name} на {self.post}"
