from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=300)

    def __str__(self):
        return self.tag


class Post(models.Model):
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="images/imgs", default="/images/defult.jpg")
    headline = models.CharField(max_length=300, null=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.headline


class Message(models.Model):
    name = models.CharField(max_length=300, default="default")
    subject = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(max_length=300, null=True)
