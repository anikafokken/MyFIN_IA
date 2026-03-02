from django.urls import path, include

from .views import SignUpView, LoginViews
from core.views import portal_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginViews.as_view(), name='login'),
    path('portal/', include('portal.urls')),
    path('portal_view/', portal_view, name='portal_view')
]