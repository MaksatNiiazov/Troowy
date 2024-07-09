from django.urls import path

from apps.authentication.api.views import (
    UserLoginView,
    VerifyCodeView,
    UserAddressCreateAPIView,
    UserAddressUpdateAPIView,
    UserAddressDeleteAPIView,
    UserDeleteAPIView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_registration'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify_code'),
    path('addresses/', UserAddressCreateAPIView.as_view(), name='create_address'),
    path('addresses/<int:pk>/update/', UserAddressUpdateAPIView.as_view(), name='update_address'),
    path('addresses/<int:pk>/delete/', UserAddressDeleteAPIView.as_view(), name='delete_address'),
    path('delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]
