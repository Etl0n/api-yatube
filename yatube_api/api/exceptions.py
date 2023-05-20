from rest_framework.exceptions import APIException
from rest_framework import status


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN


class FollowExit(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
