from rest_framework import serializers
from .models import Transport


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        # fields = '__all__'
        fields = ['name', 'price_confort', 'price_econ', 'city', 'duration', 'seat', 'bed']