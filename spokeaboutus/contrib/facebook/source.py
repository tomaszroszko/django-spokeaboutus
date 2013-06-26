import facebook as fbsdk
from spokeaboutus.contrib.spokesource import SpokeSource, SpokeMessage
from .settings import FACEBOOK_ACCESS_TOKEN


class FacebookSource(SpokeSource):
    """
        Collect posts from facebook...
    """

    name = 'Facebook'
    slug = 'facebook'

    def get_messages_user(self, search):
        """
            return posts from user account
        """
        return self.get_api().get_connections(search, 'feed')['data']

    def get_messages_search(self, search):
        """
            return posts of founded searches
        """
        return self.get_api().request('search',
            args={'q': search, 'type': 'post'})['data']

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
        spoke_link = 'http://www.facebook.com/permalink.php?id=%s&v=wall&story_fbid=%s' %(message['from']['id'], message['id'].split('_')[1])
        return SpokeMessage(
            uid=message['id'],
            author=message['from']['name'],
            about_us=message.get('message', '') or message.get(
                'description', ''),
            spoke_date=message['created_time'],
            image=message.get('picture', None),
            spoke_link=spoke_link
        )