from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_images/', verbose_name='изображение', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='дата создания', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.create_date} {self.is_published}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'