from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Report(models.Model):
    reporter = models.ForeignKey(User,
                                 related_name="reports_created",
                                 on_delete=models.CASCADE
                                 )
    category = models.ForeignKey(Category,
                                 related_name="reports",
                                 on_delete=models.CASCADE
                                 )
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
