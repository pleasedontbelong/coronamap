import os
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from base.models import Entry


CSV_MAP = (
    'date_reported',
    'country_code',
    'country',
    'who_region',
    'new_cases',
    'cumulative_cases',
    'new_deaths',
    'cumulative_deaths',
)


class Command(BaseCommand):
    help = 'Imports the data from the csv file'

    def handle(self, *args, **options):
        file = os.path.join(
            settings.ROOT,
            'apps', 'base', 'data',
            'WHO-COVID-19-global-data.csv'
        )
        Entry.objects.all().delete()
        with open(file) as csvfile:
            raw_data = csv.reader(csvfile, delimiter=',')
            # skip header
            next(raw_data)
            for row in raw_data:
                attrs = {
                    CSV_MAP[i]: value
                    for i, value in enumerate(row)
                }
                attrs['date_reported'] = datetime.strptime(
                    attrs['date_reported'], '%Y-%m-%dT%H:%M:%SZ')
                Entry(**attrs).save()
