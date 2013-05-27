from django.conf import settings

PAGINATE_BY = getattr(settings, 'SPOKE_ABOUT_US_PAGINATE_BY', 6)
