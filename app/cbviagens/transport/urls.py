from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransportViewSet

# from . import views

router = DefaultRouter()
router.register(r'transport', TransportViewSet)

app_name = 'transport'

urlpatterns = [
    path('', include(router.urls)),
]