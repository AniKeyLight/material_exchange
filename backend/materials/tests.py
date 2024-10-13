"""
Не знаю, что здесь не так, классическим запуском сервера все отображается.
python manage.py runserver
1. Перейди по адресу http://127.0.0.1:8000/admin/.
Если ты видишь страницу входа в админку, значит, всё работает.
2. Открой браузер и перейди по адресу http://127.0.0.1:8000/api/materials/.
Если ты настроил представления и маршруты правильно, ты увидишь ответ от сервера.
"""


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Material, Seller
from .serializers import MaterialSerializer

class MaterialTests(APITestCase):
    def setUp(self):
        self.seller = Seller.objects.create(name='Test Seller')
        self.material = Material.objects.create(name='Test Material', seller=self.seller, price=10.99)

    def test_create_material(self):
        """
        Проверяем, что можно создать новый материал.
        """
        url = reverse('material-list-create')
        data = {
            'name': 'New Material',
            'seller': self.seller.id,
            'price': 15.99
        }
        serializer = MaterialSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)  # Проверка, если сериализатор валиден
        response = self.client.post(url, data, format='json')
        print('Создание нового материала', response.data)  # Добавьте эту строку, чтобы увидеть ошибку
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Material.objects.count(), 2)
        self.assertEqual(Material.objects.get(name='New Material').price, 15.99)

    def test_list_materials(self):
        """
        Проверяем, что можно получить список всех материалов.
        """
        url = reverse('material-list-create')
        response = self.client.get(url)
        print('Список всех материалов', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Material')

    def test_retrieve_material(self):
        """
        Проверяем, что можно получить информацию о конкретном материале.
        """
        url = reverse('material-detail', args=[self.material.id])
        response = self.client.get(url)
        print('Получение информации о конкретном материале', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Material')

    def test_update_material(self):
        """
        Проверяем, что можно обновить информацию о материале.
        """
        url = reverse('material-detail', args=[self.material.id])
        data = {
            'name': 'Updated Material',
            'seller': self.seller.id,
            'price': 20.99
        }
        response = self.client.put(url, data, format='json')
        print('Обновление информации о материале', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.material.refresh_from_db()
        self.assertEqual(self.material.name, 'Updated Material')
        self.assertEqual(self.material.price, 20.99)

    def test_delete_material(self):
        """
        Проверяем, что можно удалить материал.
        """
        url = reverse('material-detail', args=[self.material.id])
        response = self.client.delete(url)
        print('Удаление материала', response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.count(), 0)

class SellerTests(APITestCase):
    def setUp(self):
        self.seller = Seller.objects.create(name='Test Seller')

    def test_create_seller(self):
        """
        Проверяем, что можно создать нового продавца.
        """
        url = reverse('seller-list-create')
        data = {
            'name': 'New Seller'
        }
        response = self.client.post(url, data, format='json')
        print('Создание нового продавца', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Seller.objects.count(), 2)
        self.assertEqual(Seller.objects.get(name='New Seller').name, 'New Seller')

    def test_list_sellers(self):
        """
        Проверяем, что можно получить список всех продавцов.
        """
        url = reverse('seller-list-create')
        response = self.client.get(url)
        print('Список всех продавцов', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Seller')

    def test_retrieve_seller(self):
        """
        Проверяем, что можно получить информацию о конкретном продавце.
        """
        url = reverse('seller-detail', args=[self.seller.id])
        response = self.client.get(url)
        print('Информация о конкретном продавце', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Seller')

    def test_update_seller(self):
        """
        Проверяем, что можно обновить информацию о продавце.
        """
        url = reverse('seller-detail', args=[self.seller.id])
        data = {
            'name': 'Updated Seller'
        }
        response = self.client.put(url, data, format='json')
        print('Обновление информации о продавце', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.seller.refresh_from_db()
        self.assertEqual(self.seller.name, 'Updated Seller')

    def test_delete_seller(self):
        """
        Проверяем, что можно удалить продавца.
        """
        url = reverse('seller-detail', args=[self.seller.id])
        response = self.client.delete(url)
        print('Удаление продавца', response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Seller.objects.count(), 0)
