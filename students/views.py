from rest_framework import viewsets
from .models import Student, Program, SecondaryProgram
from .serializers import (
    StudentSerializer,
    ProgramSerializer,
    SecondaryProgramSerializer
)


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class SecondaryProgramViewSet(viewsets.ModelViewSet):
    queryset = SecondaryProgram.objects.all()
    serializer_class = SecondaryProgramSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer