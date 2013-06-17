import hashlib
import feedparser
from dateutil import parser as date_parser
from spokeaboutus.contrib.spokesource import SpokeSource, SpokeMessage


class InstagramSource(SpokeSource):
    """
        Collect posts from facebook...
    """

    name = 'Instagram'
    slug = 'instagram'

    def get_messages(self):
        """
            return posts from fb
        """
        feed = 'http://instagram.com/tags/%s/feed/recent.rss' \
               % self.spoke_source.search_query
        return feedparser.parse(feed)['entries']


    def prepare_message(self, message):
        """
            convert posts to standard message
        """
        return SpokeMessage(
            uid=hashlib.sha224(message['id']).hexdigest()[:50],
            author='Uknowed',
            about_us=unicode(message['title']),
            spoke_date=date_parser.parse(message['published']),
            image=message['media_content'][0]['url']
        )