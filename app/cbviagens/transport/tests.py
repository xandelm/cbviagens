from django.test import TestCase

from django.core.management import call_command
from transport.models import Transport

# Create your tests here.

class LoadDataCommandTestCase(TestCase):
    def setUp(self):
        pass

    def test_command_output(self):
        call_command('load_data')

        transport = Transport.objects.all()
        self.assertNotEqual(transport.count(), 0)

        first_transport = transport.first()
        self.assertEqual(first_transport.name, 'Expresso Oriente')
        
