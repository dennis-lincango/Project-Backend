from rest_framework import routers
from .views import CourseViewSet, StudentViewSet, InstructorViewSet, CompanyViewSet

router = routers.DefaultRouter()

router.register('api/courses', CourseViewSet, 'courses')
router.register('api/students', StudentViewSet, 'students')
router.register('api/instructors', InstructorViewSet, 'instructors')
router.register('api/companies', CompanyViewSet, 'companies')

urlpatterns = router.urls
