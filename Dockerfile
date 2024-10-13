
# Используем официальный образ Python
FROM python:3.10

# Устанавливаем переменные окружной среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/
# Копируем код приложения
COPY backend/ /app/backend/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска вашего приложения
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]

