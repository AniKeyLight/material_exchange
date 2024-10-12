"""
Этот файл определяет URL-маршруты для приложения "materials", включая маршруты для получения списка материалов,
создания, обновления и удаления материалов
"""

from django.urls import path
from .views import MaterialListCreateAPIView, MaterialRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('materials/', MaterialListCreateAPIView.as_view(), name='material-list-create'),
    # Получение списка материалов и создание нового
    path('materials/<int:pk>/', MaterialRetrieveUpdateDestroyAPIView.as_view(), name='material-detail'),
    # Получение, обновление и удаление материала по ID
]