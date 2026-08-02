from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    ProgramViewSet,
    SecondaryProgramViewSet
)

router = DefaultRouter()

router.register(r'programs', ProgramViewSet)
router.register(r'secondary-programs', SecondaryProgramViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]