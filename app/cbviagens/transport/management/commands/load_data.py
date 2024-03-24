import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from transport.models import Transport
from decimal import Decimal
import datetime

# '../../../../../data.json'
class Command(BaseCommand):
    help = 'Load data from JSON file to database'
    data_file = os.path.join(settings.BASE_DIR,  'transport', 'management', 'commands', 'data.json')
    def handle(self, *args, **options):
        with open(self.data_file) as f:
            data = json.load(f)
            for item in data["transport"]:
                print(type(item))
                print(item)
                transport = Transport()
                transport.name = item['name']
                transport.price_confort = Decimal(item['price_confort'].replace('R$','').replace(',','.'))
                transport.price_econ =  Decimal(item['price_econ'].replace('R$','').replace(',','.'))
                transport.city = item['city']

                duration_parts = item['duration'].replace('h', '').split(':')
                hours = int(duration_parts[0])
                minutes = int(duration_parts[1]) if len(duration_parts) > 1 else 0
                transport.duration = datetime.timedelta(hours=hours, minutes=minutes)
                transport.seat = item['seat']
                transport.bed = item['bed']
                transport.save()
                self.stdout.write(self.style.SUCCESS(f'Loaded data {transport.name} Successfully!'))
