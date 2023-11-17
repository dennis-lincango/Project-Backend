from rest_framework import serializers
from .models import Course, Student, Instructor, Company


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'type', 'cost', 'description', 'necessary_knowledge')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'password')


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id', 'name', 'email', 'password', 'course', 'student')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'direction', 'image', 'city', 'description', 'course', 'instructor')

    # def create(self, validated_data):
    #     return Course.objects.create(**validated_data)
