from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Group(models.Model):
    title = models.CharField("group title", max_length=200)
    slug = models.SlugField("unique url fragment", unique=True)
    description = models.TextField("description of the group")

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )

    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="posts",
    )

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text
