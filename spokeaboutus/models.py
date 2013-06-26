from django.db import models
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from .managers import SpokeAboutUsManager, SpokeSourceManager
from .settings import SPOKE_SOURCES

#load all sources
from spokeaboutus.utils import get_source

SOURCES = [import_module(s).SPOKE_SOURCE for s in SPOKE_SOURCES]
SOURCE_CHOICES = [(s.slug, s.name) for s in SOURCES]


class SpokeSource(models.Model):
    """
        Model to store all configs
    """

    spoke_source = models.CharField(_('Spoke Source'), max_length=50,
        choices=SOURCE_CHOICES, null=True, blank=True,
        default=SOURCE_CHOICES[0])
    limit = models.IntegerField(_('Limit'), null=True, blank=True)
    search_query = models.CharField(_('Search Query'), max_length=255,
        null=True, blank=True)

    periodicity = models.IntegerField(_('Periodicy'), default=60,
        help_text=_('Collecting messages periodicy. (In minutes)'))
    is_active = models.BooleanField(_('Is Active'), default=True)
    updated = models.DateTimeField(_('Last Updated'), null=True, blank=True)

    objects = SpokeSourceManager()

    class Meta:
        verbose_name = _('Spoke Source')
        verbose_name_plural = _('Spoke Sources')

    def __unicode__(self):
        return self.get_spoke_source_display()

    def can_update(self):
        """
            return True if source is possible to update
        """
        current = now()
        return self.is_active and (self.updated is None or current > self.updated)

    @property
    def source_class(self):
        return get_source(self.spoke_source)


class SpokeAboutUs(models.Model):
    """
        Nice message about our service :)
    """
    spoke_source_uid = models.CharField(_('Spoke Source UID'), max_length=255,
        editable=False)
    spoke_source = models.ForeignKey(SpokeSource)
    spoke_link = models.CharField(_('Spoke link'), null=True, blank=True,
        max_length=255)

    author = models.CharField(_('Author'), max_length=50)
    about_us = models.TextField(_('About us'))
    image = models.ImageField(
        _('Image'), upload_to='spoke_about_us', null=True, blank=True)
    spoke_date = models.DateTimeField(_('Spoke Date'), null=True, blank=True)
    order = models.IntegerField(_('Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)

    objects = SpokeAboutUsManager()

    class Meta:
        verbose_name = _('Spoke about us')
        verbose_name_plural = _('Spokes about us')
        ordering = ('order',)

    def __unicode__(self):
        return u'%s - %s' % (self.spoke_source, self.author)
