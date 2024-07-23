from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.medical_tours.api.v1.urls'))

]
