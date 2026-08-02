from django.db import models

# Primary Program
class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Secondary Program
class SecondaryProgram(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Student
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # Primary Program
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE
    )

    # Secondary Programs
    secondary_programs = models.ManyToManyField(
        SecondaryProgram,
        blank=True
    )

    def __str__(self):
        return self.name