from django.conf import settings

PAGINATE_BY = getattr(settings, 'SPOKE_ABOUT_US_PAGINATE_BY', 6)

DEFAULT_SPOKE_SOURCES = (
    'spokeaboutus.contrib.twitter',
    'spokeaboutus.contrib.facebook',
    'spokeaboutus.contrib.instagram',
)

SPOKE_SOURCES = getattr(settings, 'SPOKE_ABOUT_US_SPOKE_SOURCE',
    DEFAULT_SPOKE_SOURCES)