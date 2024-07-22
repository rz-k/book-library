from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['authentication'])
class BaseTokenObtainPairView(TokenObtainPairView):
    ...
    
@extend_schema(tags=['authentication'])
class BaseTokenRefreshView(TokenRefreshView):
    ...
    
@extend_schema(tags=['authentication'])
class BaseTokenVerifyView(TokenVerifyView):
    ...

urlpatterns = [
        path('jwt/', include(([
            path('login/', BaseTokenObtainPairView.as_view(),name="login"),
            path('refresh/', BaseTokenRefreshView.as_view(),name="refresh"),
            path('verify/', BaseTokenVerifyView.as_view(),name="verify"),
            ])), name="jwt"),
]
