import stripe
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Request
from api.serializers import RequestSerializer

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class RequestListAPIView(APIView):
    """
    View to list all requests stored in the system.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all requests.
        """
        queryset = Request.objects.all()
        serializer = RequestSerializer(instance=queryset, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        intent = stripe.PaymentIntent.create(
            amount=5099,
            currency='usd',
            payment_method="pm_card_visa",
            confirm=True,
            metadata={'integration_check': 'accept_a_payment'},
        )
        return Response(status=status.HTTP_201_CREATED)
