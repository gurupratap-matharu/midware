from rest_framework import generics

from api.models import Request
from api.serializers import RequestSerializer


class RequestListsAPIView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
