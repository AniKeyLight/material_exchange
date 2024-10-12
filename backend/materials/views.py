"""
Этот файл содержит определения ViewSet'ов для моделей "Seller" и "Material",
а также определения ListCreateAPIView и RetrieveUpdateDestroyAPIView для работы с материалами.
"""

from rest_framework import generics
from .models import Material, Seller
from .serializers import MaterialSerializer, SellerSerializer

class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class SellerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SellerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
