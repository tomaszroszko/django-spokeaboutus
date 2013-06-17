from django.db import models


class SpokeSourceManager(models.Manager):

    def published(self):
        return self.all().filter(is_active=True)

    def to_update(self):
        """
            return sources to update
        """
        queryset = self.published()
        return [source for source in queryset if source.can_update()]


class SpokeAboutUsManager(models.Manager):

    def published(self):
        return self.all().filter(is_active=True, spoke_source__is_active=True)
