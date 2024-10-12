"""
Этот файл определяет URL-маршруты для приложения. Он включает маршруты для админки Django,
маршруты приложения "materials", маршруты для получения и обновления JWT-токенов, а также
маршруты для документации API, созданной с помощью Swagger.
"""

from django.contrib import admin
from django.urls import path, include  # Импортируем include для подключения маршрутов приложения
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Импортируем классы для JWT
from drf_yasg.views import get_schema_view  # Импортируем для Swagger
from drf_yasg import openapi  # Импортируем для Swagger

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Material Exchange API",  # Заголовок API
        default_version='v1',  # Версия API
        description="API для управления товарами",  # Описание API
        terms_of_service="https://www.google.com/policies/terms/",  # Условия использования
        contact=openapi.Contact(email="contact@materialexchange.local"),  # Контактная информация
        license=openapi.License(name="BSD License"),  # Лицензия
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админки Django
    path('api/', include('materials.urls')),  # Подключение маршрутов приложения materials
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Маршрут для получения токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Маршрут для обновления токена
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc
]
