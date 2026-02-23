from django.urls import path, include

from .views import SignUpView, LoginViews

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginViews.as_view(), name='login'),
]