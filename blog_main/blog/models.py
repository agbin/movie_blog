from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='text')
    quota = models.TextField(max_length=5000, default='text')
    text = models.TextField(default='text')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    background = models.FileField(max_length=1000, upload_to='items/%Y/%m/%d', blank=False, default='empty')
    movie_image = models.FileField(max_length=1000, upload_to='items/%Y/%m/%d', blank=True, null=True, default='empty')
    movie_image_b = models.FileField(max_length=1000, upload_to='items/%Y/%m/%d', blank=True, null=True, default='empty')




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, default=3)
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    text = models.TextField()
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.IntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
