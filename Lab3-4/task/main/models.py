from django.db import models


class News(models.Model):
    title = models.CharField('name', max_length=100)
    data = models.TextField('data')
    time = models.DateTimeField()

    def __str__(self):
        return self.title
