import json
from django.core.management.base import BaseCommand
from transport.models import Transport

class Command(BaseCommand):
    help = 'Load data from JSON file to database'
    def handle(self, *args, **options):
        with open('data.json') as f:
            data = json.load(f)
            for item in data:
                transport = Transport()
                transport.name = item['name']
                transport.price_confort = item['price_confort']
                transport.price_econ = item['price_econ']
                transport.city = item['city']
                transport.duration = item['duration']
                transport.seat = item['seat']
                transport.bed = item['bed']
                transport.save()
                self.stdout.write(self.style.SUCCESS(f'Loaded data {transport.name} Successfully!'))
                