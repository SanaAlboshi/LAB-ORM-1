from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=2048, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    published_at = models.DateTimeField(default=timezone.now, verbose_name='Published Date')
    
    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title






