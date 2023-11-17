from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.CharField(max_length=100)
    necessary_knowledge = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.type + ' ' + str(self.cost)


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    image = models.BinaryField()
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
