import json
import logging
import time

from api.models import Request

logger = logging.getLogger(__name__)


class PaymentProcessorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _t = time.time()

        body_request = ''

        if request.method == 'POST':
            body_request = self.mask_sensitive_data(request)

        response = self.get_response(request)
        _t = int((time.time() - _t) * 1000)

        try:
            r = Request.objects.create(
                endpoint=request.get_full_path(),
                response_code=response.status_code,
                method=request.method,
                remote_address=self.get_client_ip(request),
                exec_time=_t,
                body_response=str(response.content),
                body_request=body_request
            )
            logger.info(r)
            logger.info(response)

        except (ValueError, AttributeError) as e:
            print(e)

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            _ip = x_forwarded_for.split(',')[0]
        else:
            _ip = request.META.get('REMOTE_ADDR')
        return _ip

    def mask_sensitive_data(self, request):
        """Masks Credit Card and CVV info before storing into the DB"""

        data = json.loads(request.body)
        raw_cc_num, raw_cvv = data['cc_num'], data['cvv']

        masked_cc_num = len(raw_cc_num[:-4]) * 'X' + raw_cc_num[-4:]
        masked_cvv = len(raw_cvv) * 'X'

        data['cc_num'], data['cvv'] = masked_cc_num, masked_cvv
        return json.dumps(data)
