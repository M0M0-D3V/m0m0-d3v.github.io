from django.contrib import admin
from django.urls import path, include
# Register your models here.
from portfolio_app.models import Project, Message, Image, Tech, TeamMember


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class TechAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tech, TechAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(TeamMember, TeamMemberAdmin)
