from django.db import models

class Post(models.Model):
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Наименование',max_length=200)
    description = models.CharField(max_length=200,
                                   verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title