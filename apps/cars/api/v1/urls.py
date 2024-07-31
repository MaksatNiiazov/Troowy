from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.CityListView.as_view(), name='city-list'),
    path('places/', views.PlaceListView.as_view(), name='place-list'),
    path('cars/', views.CarListView.as_view(), name='car-list'),
    path('tariffs/', views.TariffListView.as_view(), name='tariff-list'),
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('service_types/', views.ServiceTypeListView.as_view(), name='service-type-list'),
    path('bids/', views.BidListView.as_view(), name='bid-list'),
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
]
