from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=True, default='')


class Category(models.Model):
    post = models.ForeignKey('Post', related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)