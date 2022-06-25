from django.db import models


class News(models.Model):
    title = models.CharField('name', max_length=100, unique=True)
    data = models.TextField('data')
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(default='no_image.jpg', upload_to='product.image')

    def __str__(self):
        return self.title
