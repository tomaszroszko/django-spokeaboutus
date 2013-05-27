from django.views.generic import ListView
from .models import SpokeAboutUs


class SpokeAboutUsListView(ListView):
    model = SpokeAboutUs
