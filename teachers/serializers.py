from rest_framework import serializers
from .models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'