from django.conf import settings
from storages.backends.s3boto3 import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = settings_STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = settings_MEDIAFILES_LOCATION