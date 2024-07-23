from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.properties.api.v1.urls')),
    path('api/v2/', include('apps.properties.api.v2.urls'))

]
