from django.core.management.base import BaseCommand
from django.utils.timezone import now
from spokeaboutus.models import SpokeSource


class Command(BaseCommand):
    help = 'Collect messages from socia servies'

    def handle(self, *args, **options):
        sources = SpokeSource.objects.to_update()
        for source in sources:
            self.stdout.write('Processing source: "%s"' % source)
            sc = source.source_class(spoke_source=source)
            sc.collect_messages()
            source.updated = now()
            source.save()
