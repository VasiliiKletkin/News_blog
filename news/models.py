from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class New(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(
        upload_to='news/', blank=True, null=True, verbose_name="Изображение")
    tags = TaggableManager()
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    publish = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации")
    views = models.ManyToManyField(
        Ip, related_name="post_views", blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse('news:new_detail', args=[self.id])
