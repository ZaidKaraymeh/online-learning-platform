from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course', views.course_detail, name='course-detail'),
]
