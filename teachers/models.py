from django.db import models
from django.contrib.auth.models import User
from students.models import Student


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name