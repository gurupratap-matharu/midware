from django.urls import path

from api.views import RequestListAPIView

urlpatterns = [
    path('', RequestListAPIView.as_view()),
]
