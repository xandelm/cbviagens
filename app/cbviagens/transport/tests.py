from django.test import TestCase

from django.core.management import call_command
from transport.models import Transport

from django.urls import reverse
from rest_framework import status

from datetime import timedelta
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
        


class TransportTests(TestCase):
    def setUp(self):
        self.transport = Transport.objects.create(
            name='Expresso Oriente',
            price_confort=100,
            price_econ=50,
            city='Porto',
            duration=timedelta(hours=5),
            seat='20',
            bed='5'
        )

    def test_transport(self):
        transport = Transport.objects.get(name='Expresso Oriente')
        self.assertEqual(transport.name, 'Expresso Oriente')
        self.assertEqual(transport.price_confort, 100)
        self.assertEqual(transport.price_econ, 50)
        self.assertEqual(transport.city, 'Porto')
        self.assertEqual(transport.duration, timedelta(hours=5))
        self.assertEqual(transport.seat, '20')
        self.assertEqual(transport.bed, '5')
        response = self.client.get(reverse('transport-detail', kwargs={'pk': self.transport.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Expresso Oriente')

    def test_create_transport(self):
        transport_data = {
            'name': 'Test Transport',
            'price_confort': 200,
            'price_econ': 100,
            'city': 'Test City',
            'duration': timedelta(hours=2),
            'seat': '10',
            'bed': '2'
        }
        response = self.client.post(reverse('transport-list'), transport_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test Transport')

        def test_update_transport(self):
            update_data = {'name': 'Updated Transport'}
            response = self.client.put(reverse('transport-detail', kwargs={'pk': self.transport.id}), update_data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['name'], 'Updated Transport')

        def test_delete_transport(self):
            response = self.client.delete(reverse('transport-detail', kwargs={'pk': self.transport.id}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)