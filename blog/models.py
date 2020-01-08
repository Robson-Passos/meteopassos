from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField(default='')
    content = RichTextUploadingField(default='')
    author = models.ForeignKey(User, default='', on_delete=models.PROTECT)
    created_at = models.DateField(default=timezone.now)   
    CategoryChoice = models.TextChoices('Category', 'ARTICLE TUTORIAL')
    category = models.CharField(blank=True, choices=CategoryChoice.choices, max_length=10)
    
    tags = TaggableManager()

    def __str__(self):
        return self.title

