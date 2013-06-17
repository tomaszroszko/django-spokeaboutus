import hashlib
import os
import urllib2

from django.core.files.base import ContentFile


class SpokeSource(object):
    """
        Base class for all spoke sources (twitter, fb...)
    """
    name = None
    slug = None

    def __init__(self, spoke_source):
        self.spoke_source = spoke_source

    def collect_messages(self):
        messages = self.get_messages()
        messages = [self.prepare_message(message) for message in messages]
        for message in messages:
            message.save(spoke_source=self.spoke_source)

    def get_messages(self):
        raise NotImplementedError

    def prepare_message(self, message):
        raise NotImplementedError



class SpokeMessage(object):

    def __init__(self, uid, author=None, about_us=None, image=None,
                 spoke_date=None):
        self.uid = uid
        self.author = author
        self.about_us = about_us
        self.image = image
        self.spoke_date = spoke_date

    def save(self, spoke_source):
        """
            Return SpokeAboutUs instance
        """
        from spokeaboutus.models import SpokeAboutUs

        try:
            sau = SpokeAboutUs.objects.get(
                spoke_source_uid=self.uid, spoke_source=spoke_source)
        except SpokeAboutUs.DoesNotExist:
            sau = SpokeAboutUs(
                spoke_source_uid = self.uid,
                spoke_source = spoke_source,
                author = self.author,
                about_us = self.about_us,
                spoke_date = self.spoke_date
            )
            if self.image:
                try:
                    base_file_name = os.path.basename(self.image)
                    file_ext = base_file_name.split('.')[-1]
                    file_name = hashlib.sha224(base_file_name).hexdigest()[:50]
                    file_name += '.' + file_ext
                    downloaded = urllib2.urlopen(self.image).read()
                    image_file = ContentFile(downloaded, name=file_name)
                    sau.image.save(file_name, image_file)
                except Exception, e:
                    pass

            #by default make it as unactive
            sau.is_active = False
            sau.save()
        return sau

