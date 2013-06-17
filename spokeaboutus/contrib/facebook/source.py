import facebook as fbsdk
from spokeaboutus.contrib.spokesource import SpokeSource, SpokeMessage
from .settings import FACEBOOK_ACCESS_TOKEN


class FacebookSource(SpokeSource):
    """
        Collect posts from facebook...
    """

    name = 'Facebook'
    slug = 'facebook'

    def get_messages(self):
        """
            return posts from fb
        """
        api = self.get_api()
        messages = api.request('search',
            args={'q': self.spoke_source.search_query, 'type': 'post'})
        return messages['data']

    def get_api(self):
        """
            return authenticated connections with fb
        """
        api = fbsdk.GraphAPI(FACEBOOK_ACCESS_TOKEN)
        return api

    def prepare_message(self, message):
        """
            convert posts to standard message
        """
        return SpokeMessage(
            uid=message['id'],
            author=message['from']['name'],
            about_us=message.get('message', '') or message.get(
                'description', ''),
            spoke_date=message['created_time'],
            image=message.get('picture', None)
        )