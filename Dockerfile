# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY Medical_Site/app/requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем все содержимое директории app
COPY Medical_Site/app /app/

