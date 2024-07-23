from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.models import (
    User,
    UserAddress
)
from apps.authentication.utils import (
    send_sms,
    generate_confirmation_code,
)
from .serializers import (
    CustomUserSerializer,
    VerifyCodeSerializer,
    UserAddressSerializer,
    UserAddressUpdateSerializer,

)

class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Требуется указать номер телефона.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(phone_number) != 13:
            return Response({'error': 'Номер телефона должен состоять из 13 цифр, включая код страны.'},
                            status=status.HTTP_400_BAD_REQUEST)
        elif not phone_number[4:].isdigit():
            return Response(
                {'error': 'Недопустимые символы в номере телефона. После кода страны допускаются только цифры.'},
                status=status.HTTP_400_BAD_REQUEST)

        confirmation_code = generate_confirmation_code()
        send_sms(phone_number, confirmation_code)

        User.objects.update_or_create(
            phone_number=phone_number,
            defaults={'code': confirmation_code}
        )

        response_data = {
            'message': 'Код подтверждения успешно отправлен.',
            'code': confirmation_code
        }
        return Response(response_data, status=status.HTTP_200_OK)


class VerifyCodeView(generics.CreateAPIView):
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        fcm_token = serializer.validated_data.get('fcm_token')
        receive_notifications = serializer.validated_data.get('receive_notifications')

        user = User.objects.filter(code=code).first()
        if not user:
            return Response({'error': 'Неверный код подтверждения.'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_verified = True
        user.code = None

        if fcm_token is not None:
            user.fcm_token = fcm_token
        if receive_notifications is not None:
            user.receive_notifications = receive_notifications

        user.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh),
            'first_visit': user.first_visit
        }, status=status.HTTP_200_OK)


class UserAddressCreateAPIView(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserAddress.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return Response({'message': 'Адрес успешно создан.'})


class UserAddressUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        if serializer.validated_data.get('is_primary', False):
            UserAddress.objects.filter(user=user, is_primary=True).update(is_primary=False)
        serializer.save()
        return Response({'message': 'Адрес успешно обновлен.'})


class UserAddressDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserAddress.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Адрес успешно удален.'}, status=status.HTTP_204_NO_CONTENT)


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()  # Удаляем пользователя

        return Response({'message': 'Пользователь удален успешно.'}, status=status.HTTP_204_NO_CONTENT)
0