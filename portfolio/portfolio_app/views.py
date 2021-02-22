from django.shortcuts import render
from .models import Project, Image, Tech, TeamMember, Message
# Create your views here.


def index(request):
    context = {
        "all_projects": Project.objects.all()
    }
    return render(request, "index.html", context)
