from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TransportSerializer
from .models import Transport

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all().order_by('name')
    serializer_class = Transport




# from django.shortcuts import render
# from .forms import TransportForm

# def transport(request):
#     if request.method == 'POST':
#         form = TransportForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/transport/')
#     else:
#         form = TransportForm()
#
#     return render(request, 'transport/transport.html', {'form': form})