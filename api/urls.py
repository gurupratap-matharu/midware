from django.urls import path

from api.views import RequestListsAPIView

urlpatterns = [
    path('', RequestListsAPIView.as_view()),
]
