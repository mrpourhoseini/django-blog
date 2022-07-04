from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    active = models.BooleanField(verbose_name="active")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft'
        PUBLISHED = 'published'

    title = models.CharField(max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, null=False, allow_unicode=True, verbose_name="slug")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    lead = models.TextField(null=True, blank=True, verbose_name="lead")
    body = models.TextField(verbose_name="body")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    featured = models.BooleanField(default=False, verbose_name="featured")

    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="created")
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default=StatusChoices.DRAFT,
                              verbose_name="status")
    publish_time = models.DateTimeField(verbose_name="publish time")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-publish_time']
