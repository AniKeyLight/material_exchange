"""
Этот файл определяет URL-маршруты для приложения "materials", включая маршруты для получения списка материалов,
создания, обновления и удаления материалов
"""

from django.urls import path
from .views import MaterialListCreateAPIView, MaterialRetrieveUpdateDestroyAPIView, SellerListCreateAPIView, SellerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('materials/', MaterialListCreateAPIView.as_view(), name='material-list-create'),
    # Получение списка материалов и создание нового
    path('materials/<int:pk>/', MaterialRetrieveUpdateDestroyAPIView.as_view(), name='material-detail'),
    # Получение, обновление и удаление материала по ID
    path('sellers/', SellerListCreateAPIView.as_view(), name='seller-list-create'),
    path('sellers/<int:pk>/', SellerRetrieveUpdateDestroyAPIView.as_view(), name='seller-detail'),
]