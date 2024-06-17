import datetime
import os


def build_django_rest_framework(your_settings=None):
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],
        'ACCESS_TOKEN_LIFETIME': datetime.timedelta(
            days=int(os.getenv('ACCESS_TOKEN_DAYS', '10')),
            minutes=int(os.getenv('ACCESS_TOKEN_MINUTES', '60')),
            seconds=int(os.getenv('ACCESS_TOKEN_SECONDS', '0')),
        ),
        'REFRESH_TOKEN_LIFETIME': datetime.timedelta(
            days=int(os.getenv('REFRESH_TOKEN_DAYS', '12')),
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 20,
        'DEFAULT_FILTER_BACKENDS': [
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter'
        ],
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',
        ],
        'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }
    if your_settings:
        REST_FRAMEWORK.update(your_settings)

    return REST_FRAMEWORK
