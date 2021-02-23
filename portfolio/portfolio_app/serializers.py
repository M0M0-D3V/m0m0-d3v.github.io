from rest_framework_json_api import serializers
from portfolio_app.models import Project, Message, Image, Tech, TeamMember


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'demo_link', 'github_link',
                  'publish_date', 'my_position')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Image
        fields = ('url', 'project')


class TechSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Tech
        fields = ('tech_name', 'icon_img_url', 'projects')


class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: TeamMember
        fields = ('member_name', 'member_role', 'projects')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Message
        fields = ('body', 'sender_name', 'sender_email', 'subject')
