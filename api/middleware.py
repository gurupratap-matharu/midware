import logging
import time

from api.models import Request

logger = logging.getLogger(__name__)


class PaymentProcessorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _t = time.time()
        response = self.get_response(request)
        _t = int((time.time() - _t) * 1000)

        logger.info(request)
        logger.info(response)

        try:
            Request(
                user=request.user,
                endpoint=request.get_full_path(),
                response_code=response.status_code,
                method=request.method,
                remote_address=self.get_client_ip(request),
                exec_time=_t,
                body_response=str(response.content),
                body_request=str(request.body)
            ).save()

        except (ValueError, AttributeError):
            pass

        return response
