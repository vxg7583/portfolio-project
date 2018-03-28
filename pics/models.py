from django.db import models

# Create your models here.


# Create your models here.
class Pic(models.Model):
    body = models.TextField(max_length="255")
    image = models.ImageField(upload_to = 'images/')
    title = models.TextField(max_length="255")

    def summary(self):
        return self.body[:300]


    def __str__(self):
        return self.title
