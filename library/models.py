from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class BookQuerySet(models.QuerySet):
    def search(self, search_query):
        return self.filter(
            Q(name__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(genre__icontains=search_query) |
            Q(review__icontains=search_query) |
            Q(rating__icontains=search_query)
        )


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def search(self, search_query):
        return self.get_queryset().search(search_query)


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=220, null=True)
    author = models.CharField(max_length=220, null=True)
    genre = models.CharField(max_length=100, null=True)
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BookManager()

    class Meta:
        ordering = ['-id']
