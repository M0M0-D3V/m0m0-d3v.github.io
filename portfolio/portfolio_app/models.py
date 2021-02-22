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

    def __repr__(self):
        return f"{self.id} - {self.title}"

    def __str__(self):
        return f"{self.id} - {self.title}"


class Image(models.Model):
    url = models.CharField(max_length=255)
    # PROJECT FOREIGN KEY
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tech(models.Model):
    tech_name = models.CharField(max_length=45)
    projects = models.ManyToManyField(
        Project, related_name="techs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TeamMember(models.Model):
    member_name = models.CharField(max_length=100)
    member_role = models.CharField(max_length=45)
    projects = models.ManyToManyField(
        Project, related_name="members")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    body = models.TextField()
    sender_name = models.CharField(max_length=45)
    sender_email = models.CharField(max_length=100)
    subject = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
