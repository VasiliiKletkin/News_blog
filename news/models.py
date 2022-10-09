from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


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

    def get_absolute_url(self):
        return reverse('news:new_detail', args=[self.id])
            
class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ('-publish',)


def __str__(self):
    return self.title
