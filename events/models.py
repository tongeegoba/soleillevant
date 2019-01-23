from django.db import models
from django.utils import timezone
# Create your models here.


class Event(models.Model):

    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    def like(self):
        self.likes += 1
        self.save()


class Comment(models.Model):

    event =models.ForeignKey(Event, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)