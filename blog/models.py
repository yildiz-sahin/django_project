from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tag = models.CharField(max_length=20, blank=True)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def success_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment = models.TextField()
    # post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self):
        super().save()

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})

    def success_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})
