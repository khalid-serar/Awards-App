from rest_framework import serializers
from .models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_title', 'project_image', 'project_description', 'project_link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( 'profile_picture','profile_bio','profile_contact','user')