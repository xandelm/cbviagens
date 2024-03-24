from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TransportSerializer
from .models import Transport




from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view


from datetime import datetime
def parse_duration(duration):
    total_seconds = duration.total_seconds()
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    duration_str = f'{int(hours)}H:{int(minutes)}M:{int(seconds)}S'
    duration_str = ''
    if(seconds == 0):
        duration_str =  f'{int(hours)}H:{int(minutes)}M'
        if (minutes == 0):
            duration_str =  f'{int(hours)}H'
    return duration_str

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer



@api_view(['GET'])
def get_best_transport_options(request):
        city = request.GET.get('city', None)
        if not city:
            return JsonResponse({'message': 'city is required'}, status=400)
        try:
            confort_option = Transport.objects.filter(city=city).order_by('duration', 'price_confort').first()
            econ_option = Transport.objects.filter(city=city).order_by('price_econ').first()
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'No transport available for this city'}, status=404)
        if not confort_option or not econ_option:
            return JsonResponse({'message': 'No transport available for this city'}, status=404)
        confort_option_duration_str = parse_duration(confort_option.duration)
        econ_option_duration_str = parse_duration(econ_option.duration)
        return JsonResponse({
            'confort':{
                'name': confort_option.name,
                'price_confort': confort_option.price_confort,
                'price_econ': confort_option.price_econ,
                'city': confort_option.city,
                'duration': confort_option_duration_str,
                'seat': confort_option.seat,
                "bed": confort_option.bed
            },
            'econ':{
                'name': econ_option.name,
                'price_confort': econ_option.price_confort,
                'price_econ': econ_option.price_econ,
                'city': econ_option.city,
                'duration':  econ_option_duration_str,
                'seat':econ_option.seat ,
                "bed": econ_option.bed,
            }
        })