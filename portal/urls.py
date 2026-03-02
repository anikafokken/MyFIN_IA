from django.urls import include, path
from portal import views

urlpatterns = [
    path('student/', views.student_portal, name='student_portal'),
    path('institution/', views.school_portal, name='school_portal'),
    path('admin/', views.admin_portal, name='admin_portal')
]