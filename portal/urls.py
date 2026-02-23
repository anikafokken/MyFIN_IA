from django.urls import include, path
from portal import views

urlpatterns = [
    path('/student', views.student_portal),
]