import stripe
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Request
from api.serializers import RequestSerializer

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class RequestListAPIView(APIView):
    """
    View to list all requests stored in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all requests.
        """

        return Response()

    def post(self, request, format=None):
        intent = stripe.PaymentIntent.create(
            amount=5099,
            currency='usd',
            payment_method="pm_card_visa",
            confirm=True,
            metadata={'integration_check': 'accept_a_payment'},
        )
        return Response()


class SalariesAPIView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        print('name:', name)
        if name:
            queryset = self.paginate_queryset(queryset=self.queryset.filter(name__icontains=name))
        else:
            queryset = self.paginate_queryset(queryset=self.queryset)
        serializer = SalariesSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        print('data: ', request.data)
        serializer = SalariesSerializer(data=request.data)

        intent = stripe.PaymentIntent.create(
            amount=20099,
            currency='usd',
            payment_method="pm_card_visa",
            confirm=True,
            metadata={'integration_check': 'accept_a_payment'},
        )

        print(intent)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
