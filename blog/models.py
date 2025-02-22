from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.
class PostQuerySet(models.QuerySet):
    def search(self, search_query):
        return self.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, search_query):
        return self.get_queryset().search(search_query)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['-id']


class PostSearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
