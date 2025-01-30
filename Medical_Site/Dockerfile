# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY app /app/

