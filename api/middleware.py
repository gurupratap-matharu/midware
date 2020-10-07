import logging

logger = logging.getLogger(__name__)


class PaymentProcessorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        logger.debug(request)
        logger.debug(response)

        return response
