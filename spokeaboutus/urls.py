from django.conf.urls import patterns, url
from .views import SpokeAboutUsListView
from .settings import PAGINATE_BY

urlpatterns = patterns('',
    url(r'^$', SpokeAboutUsListView.as_view(paginate_by=PAGINATE_BY),
        name="spoke_about_us"),
)