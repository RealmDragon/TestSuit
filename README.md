Дипломная работа для Сайт компании медицинской диагностики (BF2)

# Medical Site - Django Application with Docker

Этот проект представляет собой веб-приложение на Django, разработанное с использованием Docker для упрощения развертывания и управления. Приложение использует PostgreSQL в качестве базы данных и Gunicorn в качестве WSGI-сервера.

## Описание проекта

Приложение Medical Site предоставляет [опишите кратко основную функциональность вашего приложения, например, "интерфейс для управления медицинскими записями, просмотра информации о врачах и пациентах и т.д."].

## Технологии

*   **Python 3.11**: Основной язык программирования.
*   **Django 5.1**: Веб-фреймворк.
*   **PostgreSQL**: База данных.
*   **Docker**: Платформа для контейнеризации.
*   **Docker Compose**: Инструмент для оркестрации контейнеров.
*   **Gunicorn**: WSGI HTTP-сервер.
*   **Bootstrap 4**: CSS-фреймворк.
*   **psycopg2-binary**: Библиотека для работы с PostgreSQL.
*   **Pillow**: Библиотека для работы с изображениями.

## Структура проекта

medical_site/  (Project Root)
├── app/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_department_doctor.py
│   │   └── 0003_medicalservice.py
│   │   └── __init__.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── Backgroundmed.jpg
│   │   │   └── styles.css
│   │   ├── js/
│   │   └── vendor/
│   ├── templates/
│   │   ├── admin/
│   │   ├── about.html
│   │   ├── add_doctor.html
│   │   ├── appointment.html
│   │   ├── contacts.html
│   │   ├── delete_doctor.html
│   │   ├── departments.html
│   │   ├── doctors.html
│   │   ├── edit_doctor.html
│   │   ├── index.html
│   │   ├── profile.html
│   │   ├── registration.html
│   │   └── services.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── medical_site/ (Django Project Directory)
│   ├── materials/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── media/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/         (Virtual Environment)
├── .env
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
├── init-db.sql
├── manage.py
├── pytest.ini
├── README.md
└── requirements.txt

## Настройка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone <ссылка_на_репозиторий>
    cd <имя_репозитория>
    ```

2.  **Создайте файл `.env`:**
    *   В корне проекта создайте файл `.env` и заполните его переменными окружения (пример):
        ```env
        DATABASE_NAME=medical_site_db
        DATABASE_USER=medical_user
        DATABASE_PASSWORD=your_secure_password
        ```

3.  **Запустите приложение с помощью Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```

4.  **Проверьте работу приложения:**
    *   Откройте веб-браузер и перейдите по адресу `http://localhost:8000`.

## Настройки `settings.py`

*   В файле `Medical_Site/Medical_Site/settings.py` должны быть следующие настройки:
    *   `DEBUG = True` (для разработки) / `DEBUG = False` (для продакшена)
    *   `ALLOWED_HOSTS = ['*']` (для работы в Docker)
    *   `DATABASES` настроен для подключения к PostgreSQL с использованием переменных окружения.
    *  `STATIC_URL` и `STATICFILES_DIRS` должны соответствовать расположению статических файлов.

## Настройка базы данных

*   При первом запуске контейнера PostgreSQL, файл `init-db.sql` автоматически создает базу данных и пользователя.

## Обновление зависимостей

*   Если вы вносите изменения в `requirements.txt`, пересоберите образ, выполнив команду `docker-compose up --build -d`.

## Разработка и отладка

*   Вы можете изменить исходный код в директории `Medical_Site/app`.
*  Изменения в статических файлах (в папке `main/static`) будут применены при перезагрузке приложения.

## Полезные Docker-команды

*   `docker-compose up --build -d`: Запуск приложения.
*   `docker-compose down`: Остановка приложения.
*   `docker-compose restart`: Перезапуск контейнеров.
*   `docker ps`: Просмотр запущенных контейнеров.
*   `docker logs <container_name>`: Просмотр логов контейнера.



