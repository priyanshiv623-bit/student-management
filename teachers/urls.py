from django.urls import path
from .views import subjects


urlpatterns = [
    path('subjects/', subjects),
]