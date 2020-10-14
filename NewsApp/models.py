from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Отредактировано')
    photo = models.ImageField(upload_to='photos/%Y-%m-%D/', verbose_name='Фото')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.ImageField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
