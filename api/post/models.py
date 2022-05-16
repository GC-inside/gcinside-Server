from django.db import models
from api.accounts.models import User
from api.gallery.models import Gallery

# Create your models here.
class Post(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="post_image")
    created_at = models.DateTimeField()
    liked_user = models.ManyToManyField(User, through='Like', related_name='liked_posts')
    disliked_user = models.ManyToManyField(User, through='DisLike', related_name='disliked_posts')

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.content

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)