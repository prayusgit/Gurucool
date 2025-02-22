from django.db import models


# Create your models here.

class Grade(models.Model):
    GRADE_NAME = (
        ('eleven', 'eleven'),
        ('twelve', 'twelve')
    )
    name = models.CharField(max_length=50, null=True, choices=GRADE_NAME)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=220, null=True)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



class Numerical(models.Model):
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    chapter = models.ForeignKey(Chapter, null=True, on_delete=models.SET_NULL)
    question = models.TextField(max_length=2000, null=True)
    content = models.TextField(null=True)
