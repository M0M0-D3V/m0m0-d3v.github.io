from django.shortcuts import render
from .models import Project, Image, Tech, TeamMember, Message
from portfolio_app.serializers import ProjectSerializer, ImageSerializer, TechSerializer, TeamMemberSerializer, MessageSerializer
from rest_framework import viewsets
# Create your views here.


def index(request):
    context = {
        "all_projects": Project.objects.all()
    }
    return render(request, "index.html", context)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
