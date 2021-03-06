import tweepy
from spokeaboutus.contrib.spokesource import SpokeSource, SpokeMessage
from .settings import (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKENS_SECRET)



class TwitterSource(SpokeSource):
    """
        Collect Tweets..
    """

    name = 'Twitter'
    slug = 'twitter'

    def get_messages_user(self, search):
        """
            return tweets from user account
        """
        return self.get_api().user_timeline(
            user_id=search, count=20,
            include_entities=True, include_rts=True)

    def get_messages_search(self, search):
        """
            return tweets by search param
        """
        return self.get_api().search(
            q=search,
            count=self.spoke_source.limit)

    def get_api(self):
        """
            return authenticated connections with twitter
        """
        oauth = tweepy.OAuthHandler(
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET,
            callback=None, secure=True)
        oauth.set_access_token(TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_TOKENS_SECRET)
        return tweepy.API(oauth)

    def prepare_message(self, message):
        """
            convert tweets to standard message
        """
        #TODO: add getting images from tweet
        #https://dev.twitter.com/docs/tweet-entities

        return SpokeMessage(
            uid=message.id_str,
            author=message.user.name,
            about_us=message.text,
            spoke_date=message.created_at,
            spoke_link='https://twitter.com/%s/status/%s' % (
                message.user.screen_name, message.id_str)
            #image=
        )