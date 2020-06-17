from django.db import models

class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200, default=' ')
    content = models.TextField()
    date_published = models.DateTimeField('date published')
    slug = models.CharField(max_length=200, default='slug')

    def __str__(self):
        return self.title