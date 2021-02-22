from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    publish_date = models.DateTimeField()
    team_members = models.CharField(max_length=100)
    my_position = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    url = models.CharField(max_length=255)
    # PROJECT FOREIGN KEY
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    body = models.TextField()
    sender_name = models.CharField(max_length=45)
    sender_email = models.CharField(max_length=100)
    subject = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
