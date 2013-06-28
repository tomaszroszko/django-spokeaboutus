django-spokeaboutus
===================

SpokeAboutUs is a django application to store and display short messages about
your service


Installation
------------

``pip install -e git+https://github.com/tomaszroszko/django-spokeaboutus.git#egg=django_spokeaboutus.git``

*settings.py*

```

INSTALED_APPS = (
    ...
    'spokeaboutus',
    ...
)
```

*urls.py*

```

urlpatterns = patterns('',
    ...
    url(r'^spoke-about-us/', include('spokeaboutus.urls')),
    ...
)
```

*run commands*

```
python manage.py syncdb
python manage.py migrate
```


Default spoke sources are. Facebook, twitter and instagram.

```
DEFAULT_SPOKE_SOURCES = (
    'spokeaboutus.contrib.twitter',
    'spokeaboutus.contrib.facebook',
    'spokeaboutus.contrib.instagram',
)
```

You can overwrite spoke sources in *settings.py*

```
SPOKE_ABOUT_US_SPOKE_SOURCE = (
    'spokeaboutus.contrib.twitter',
    'spokeaboutus.contrib.facebook',
    'your.spokeaboutus.source',
)
```

Collecting messages automatically
---------------------------------

Add this command to your cron jobs:

```
    python manage.py collect_info_about_us
```


Facebook
--------

Requried settings:
SPOKE_ABOUT_US_FACEBOOK_CLIENT_ID - your app client_id
SPOKE_ABOUT_US_FACEBOOK_CLIENT_SECRET - your app client secret

Twitter
-------
SPOKE_ABOUT_US_TWITTER_CONSUMER_KEY - your app consumer key
SPOKE_ABOUT_US_TWITTER_CONSUMER_SECRET - your app consumer secret key
SPOKE_ABOUT_US_TWITTER_ACCESS_TOKEN - your app access token
SPOKEA_ABOUT_US_TWITTER_ACCESS_TOKEN_SECRET - your app access token secret

Instagram
---------
SPOKE_ABOUT_US_INSTAGRAM_ACCESS_TOKEN - your app access token


TODO:
-----

* use celery to process news
* wrote tests