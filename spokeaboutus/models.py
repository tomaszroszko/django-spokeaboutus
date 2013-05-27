from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import SpokeSourceManager, SpokeAboutUsManager


class SpokeSource(models.Model):
    """
        Twitter, Facebook...
    """
    name = models.CharField(_('Name'), max_length=50)
    icon = models.ImageField(
        _('Image'), upload_to='spoke_source_icons', null=True, blank=True)
    is_active = models.BooleanField(_('Is Active'), default=True)

    objects = SpokeSourceManager()

    class Meta:
        verbose_name = _('Spoke source')
        verbose_name_plural = _('Spoke source')

    def __unicode__(self):
        return self.name


class SpokeAboutUs(models.Model):
    """
        Nice message about our service :)
    """

    author = models.CharField(_('Author'), max_length=50)
    about_us = models.TextField(_('About us'))

    image = models.ImageField(
        _('Image'), upload_to='spoke_about_us', null=True, blank=True)
    spoke_date = models.DateTimeField(_('Spoke Date'), null=True, blank=True)
    spoke_source = models.ForeignKey(SpokeSource)
    order = models.IntegerField(_('Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)

    objects = SpokeAboutUsManager()

    class Meta:
        verbose_name = _('Spoke about us')
        verbose_name_plural = _('Spokes about us')
        ordering = ('order',)

    def __unicode__(self):
        return u'%s - %s' % (self.spoke_source.name, self.author)
