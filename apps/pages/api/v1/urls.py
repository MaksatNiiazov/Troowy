from django.urls import path

from apps.pages.api.v1.views import (
    StaticPageDetailView, WellcomePageView,

)

urlpatterns = [
    path('page/wellcome/', WellcomePageView.as_view(), name='wellcome-page'),
    path('static-pages/<slug:slug>/', StaticPageDetailView.as_view(), name='static-page-detail'),
    path('static-pages/about-us/', StaticPageDetailView.as_view(), name='about-us-page'),
]
