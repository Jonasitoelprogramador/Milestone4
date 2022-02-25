from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from .settings import STATICFILES_LOCATION, MEDIAFILES_LOCATION

class StaticStorage(S3Boto3Storage):
    location = STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = MEDIAFILES_LOCATION