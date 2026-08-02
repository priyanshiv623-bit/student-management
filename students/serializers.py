from rest_framework import serializers
from .models import Student, Program, SecondaryProgram


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class SecondaryProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryProgram
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"