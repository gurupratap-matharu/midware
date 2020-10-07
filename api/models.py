from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    endpoint = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    response_code = models.PositiveSmallIntegerField()
    method = models.CharField(max_length=10, null=True)
    remote_address = models.CharField(max_length=20, null=True)
    exec_time = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    body_response = models.TextField()
    body_request = models.TextField()

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return ", ".join(
            [
                str(self.date),
                self.method,
                self.endpoint,
                str(self.response_code),
                str(self.exec_time),
            ]
        )
