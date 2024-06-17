# Используйте базовый образ Python
FROM python:3.9

# Установите зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Скопируйте файлы приложения
COPY . /app
WORKDIR /app

# Запуск приложения с Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
