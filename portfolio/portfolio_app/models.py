from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    demo_link = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
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

    def __str__(self):
        return f"{self.id} - {self.project.title} - {self.url}"


class Tech(models.Model):
    tech_name = models.CharField(max_length=45)
    icon_img_url = models.CharField(max_length=255)
    projects = models.ManyToManyField(
        Project, related_name="techs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.tech_name}"


class TeamMember(models.Model):
    member_name = models.CharField(max_length=100)
    member_role = models.CharField(max_length=45)
    projects = models.ManyToManyField(
        Project, related_name="members")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.member_name}"


class Message(models.Model):
    body = models.TextField()
    sender_name = models.CharField(max_length=45)
    sender_email = models.CharField(max_length=100)
    subject = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
