from django.db import models
from django.contrib.auth.models import User

class Attribute(models.Model):
    name = models.TextField()
    value = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.name, self.value)

class Image(models.Model):
    image = models.ImageField()
    
    def __str__(self):
        return self.image.name

class Product(models.Model):
    name = models.TextField()
    attribute = models.ManyToManyField(Attribute)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.user, self.product)