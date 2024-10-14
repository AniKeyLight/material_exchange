
RESTful API для управления товарами на "Бирже материалов".

1. Описание проекта:
   - Material Exchage API - это RESTful API для управления товарами на "Бирже материалов".
   - Каждый товар представляет собой уникальный материал с названием, стоимостью и
   информацией о продавце, который предлагает этот товар на бирже.
   - Функциональные возможности:
     - Управление материалами и продавцами:
       - Создание
       - Обновление
       - Чтение
       - Удаление
     - Аутенфикация и авторизация пользователей с использованием JWT.

2. Технологии и инструменты:
   - Django
   - Django REST Framework 
   - Swagger (для документации API)
   - JWT (для аутентификации)
   - Docker (для контейнеризации приложения)
   - Vue.js + Axios (для frontend)

3. Установка и запуск:
   1) Клонируйте репозиторий:
   git clone https://github.com/your-username/material-exchange.git
   
   2) Перейдите в директорию с проектом:
   cd material-exchange 
   
   3) Создайте и активируйте виртуальное окружение:
   python -m venv venv
   source venv/bin/activate 
   
   4) Установите зависимости:
   pip install -r backend/requirements.txt 
   
   5) Выполните миграции:
   cd backend
   python manage.py migrate

   6) Запустите сервер:
   python manage.py runserver 
   
   7) Откройте документацию API в Swagger:
   http://localhost:8000/swagger/
   
   8) Для запуска frontend-части проекта:
   cd frontend
   npm install
   npm run serve
   
   9) Контейнеризация с помощью Docker 
      - Установите Docker и Docker Compose. 
      - Перейдите в корневую директорию проекта. 
      - Запустите контейнеры:
        docker-compose up -d

   10) Откройте документацию API в Swagger:
   http://localhost:8000/swagger/

4. Документация API:
   Полная документация API доступна по адресу /swagger/.

5. Авторизация:
   - Для авторизации используется JWT. 
   Для получения access и refresh токенов отправьте POST-запрос на /api/token/ 
   с данными пользователя.
   
   Пример запроса:
POST /api/token/
{
"username": "your_username",
"password": "your_password"
}

   Ответ будет содержать access и refresh токены:
{
"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxNTAzNDU5LCJpYXQiOjE2MjE0OTk4NTksImp0aSI6ImUyYmU4YjRmMzU2ZDQwOTg4MDU1ZTRlNDkwNmM0ZDk0IiwidXNlcl9pZCI6MX0.Xsswg_Dn9cWVIJyQQi2UMj7gpxAmHiNl4HcXvQk0mgc",
"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMTU4NjI1OSwiaWF0IjoxNjIxNDk5ODU5LCJqdGkiOiI2ZmY0OTIzNjZhMzc0NTU4YjM2ZjZhNDU2ZDUxMGU1ZCIsInVzZXJfaWQiOjF9.Ju370zwXuGKSdATp7kZLXtTNwZyHPVl_eUNBxw3Bq-k"
}

   Для доступа к защищенным ресурсам, необходимо передавать access токен в заголовке Authorization:
Authorization: Bearer <access_token>

6. Примеры использования:
   - Добавьте примеры запросов к вашему API для основных CRUD-операций.
   - Можно использовать Swagger или Postman для демонстрации примеров.

7. Структура проекта:
   - Сама структура:
   material_exchange/
│
├── backend/
│ ├── manage.py
│ ├── material_exchange/
│ │ ├── __init__.py
│ │ ├── asgi.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── materials/
│ │ ├── migrations/
│ │ │ ├── 0001_initial.py
│ │ │ ├── __init__.py
│ │ ├── __init__.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── tests.py
│ │ ├── views.py
│ │ └── urls.py
│ ├── db.sqlite3
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ └── package.json
│
├── venv/
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ └── ...
│
└── docker-compose.yml

   - Назначение основных директорий/файлов:
   
8. Планы на будущее:
   - Провести нормальное тестирование, как минимум.
   - написать фронтенд
   
9. Контакты:
   - почта: anikeylight@mail.ru
   - мессенджеры:
     - vk.com: https://vk.com/anikeylight
     - telegram: @anikeylight

