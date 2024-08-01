Тестовое задание на вакансию "Программист-разработчик Python"
# Проект test_Veclich

## Описание

Этот проект представляет собой контейнеризированное веб-приложение на FastAPI с поддержкой PostgreSQL и MongoDB, кэшированием на Redis, использованием Nginx в качестве веб-сервера и Telegram-бота, который взаимодействует с данными.

## Структура проекта

- `app/`: Директория с кодом приложения FastAPI.
  - `__init__.py`: Инициализация приложения.
  - `main.py`: Основной файл приложения.
  - `models.py`: Модели данных для PostgreSQL.
  - `routes.py`: Маршрутизация API.
  - `database.py`: Логика подключения к базам данных.
- `bot/`: Директория с кодом Telegram-бота.
  - `bot.py`: Основной файл бота.
  - `handlers.py`: Обработчики команд бота.
- `nginx/`: Директория с конфигурацией Nginx.
  - `nginx.conf`: Конфигурационный файл Nginx.
- `.env`: Файл с переменными окружения.
- `Dockerfile`: Файл для сборки Docker-образа FastAPI приложения.
- `docker-compose.yml`: Файл для управления Docker-контейнерами.
- `requirements.txt`: Список зависимостей Python.
- `README.md`: Описание проекта и инструкция по установке и использованию.

## Установка

### 1. Клонирование репозитория

Клонируйте репозиторий на ваш локальный компьютер:

```bash
git@github.com:dima-wadim/test_Veclich.git


### 2. Настройка переменных окружения

Создайте файл .env в корне проекта и заполните его необходимыми значениями:

DATABASE_URL=postgresql+asyncpg://user:password@postgres/mydatabase
MONGO_URL=mongodb://mongo:27017
REDIS_URL=redis://redis:6379

### 3. Установка зависимостей
Убедитесь, что у вас установлен Docker и Docker Compose. Затем установите зависимости, запустив контейнеры:

docker-compose up --build
### 4. Миграция базы данных PostgreSQL
Выполните миграции для PostgreSQL, чтобы инициализировать базу данных:

docker-compose exec web alembic upgrade head

## Использование
1. Веб-приложение
Приложение будет доступно по адресу http://localhost.

Доступные API эндпоинты:
GET /api/v1/messages/: Получение списка всех сообщений.
POST /api/v1/message/: Создание нового сообщения.
2. Telegram-бот
Телеграм-бот взаимодействует с вашим приложением. Для его настройки:

Создайте бота через BotFather и получите токен.
Добавьте токен в bot.py в переменную Bot(token='YOUR_TELEGRAM_BOT_TOKEN').
Дополнительные возможности
1. Кэширование с Redis
Кэширование сообщений реализовано через Redis. Кэш автоматически сбрасывается при добавлении нового сообщения.

2. SSL и деплой
Для деплоя на сервере вы можете использовать Nginx и Certbot для добавления SSL сертификатов.

3. Пагинация
Эндпоинты могут быть расширены для поддержки пагинации, что удобно для работы с большими объемами данных.


### Заключение

Теперь у вас есть полностью настроенный проект `test_Veclich`, готовый к использованию и развертыванию. Этот README файл предоставляет все необходимые инструкции для разработки, развертывания и работы с проектом.
