from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.cars.api.v1.urls'))

]
