from django.db import models
from MainPage.models import Category

# Create your models here.
class TargetAudience(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Target Audience'
        verbose_name_plural = 'Target Audiences'
        

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    main_message = models.CharField(max_length=255)
    target_audience = models.ForeignKey(TargetAudience, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='articlesImages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Subtitle(models.Model):
    article = models.ForeignKey(Article, related_name='subtitles', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=False)  
    text = models.TextField( blank=True, null=False)
    image = models.ImageField(upload_to='subtitle_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Subtitle'
        verbose_name_plural = 'Subtitles'
        
