import hashlib
import feedparser

from dateutil import parser as date_parser
from instagram.client import InstagramAPI

from spokeaboutus.contrib.instagram.settings import (
    DEFAULT_AUTHOR, INSTAGRAM_ACCESS_TOKEN)
from spokeaboutus.contrib.spokesource import SpokeSource, SpokeMessage


class InstagramSource(SpokeSource):
    """
        Collect posts from facebook...
    """

    name = 'Instagram'
    slug = 'instagram'

    def get_api(self):
        print INSTAGRAM_ACCESS_TOKEN
        api = InstagramAPI(access_token=INSTAGRAM_ACCESS_TOKEN)
        return api

    def get_messages_search(self, search):
        """
            return posts from fb
        """
        api = self.get_api()
        return api.tag_recent_media(tag_name=search)[0]

    def get_messages_user(self, search):
        """
            get messages for search username
        """
        api = self.get_api()
        user_id = api.user_search(q=search)[0].id
        return api.user_recent_media(user_id=user_id)[0]

    def prepare_message(self, message):
        """
            convert posts to standard message
        """
        return SpokeMessage(
            uid=hashlib.sha224(message.id).hexdigest()[:50],
            author=message.user.username,
            about_us=message.caption,
            spoke_date=message.created_time,
            image=message.images['standard_resolution'].url,
            spoke_link=message.link
        )