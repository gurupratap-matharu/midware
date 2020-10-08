from rest_framework import serializers

from api.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'date', 'method', 'endpoint', 'response_code',
                  'exec_time', 'remote_address', 'body_request', 'body_response',)
