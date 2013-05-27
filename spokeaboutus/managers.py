from django.db import models


class SpokeSourceManager(models.Manager):

    def published(self):
        return self.all().filter(is_active=True)


class SpokeAboutUsManager(models.Manager):

    def published(self):
        return self.all().filter(is_active=True, spoke_source__is_active=True)
