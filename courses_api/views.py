from .models import Course, Student, Instructor, Company
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer, StudentSerializer, InstructorSerializer, CompanySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InstructorSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer
