from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):

    authors = models.CharField(max_length=200,blank=False, null=False, default='Feminist')
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(blank=True,null=True, default=timezone.now, editable=False)
    published = models.BooleanField(default=False)
    likes = models.IntegerField(default=0, editable=False)

    def publish(self):
        self.published = True
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def like(self):
        self.likes += 1
        self.save()


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content