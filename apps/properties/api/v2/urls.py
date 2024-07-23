from django.urls import path

from apps.properties.api.v2.views import PropertyMainView

urlpatterns = [
    path('main/', PropertyMainView.as_view(), name='property-main'),

]
