from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/', blank=True)
    text = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title