![.github/workflows/yamdb_workflow.yml](https://github.com/luydmila-davletova/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
ссылка на развернутый проект http://158.160.14.79/redoc/
## Описание 
 
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Пользователи могут оставить к произведениям текстовые отзывы и поставить произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. Присутствует возможность комментирования отзывов.

Функционал API:
1) Просмотр произведений (кино, музыка, книги), которые подразделяются по жанрам и категориям.
2) Возможность оставлять отзывы на произведения и ставить им оценки, на основе которых построена система рейтингов.
3) Комментирование оставленных отзывов.

Настройка для приложения Continuous Integration и Continuous Deployment, реализация:
- автоматический запуск тестов,
- обновление образов на Docker Hub,
- автоматический деплой на боевой сервер при пуше в главную ветку master.

Проект разработан командой из трех человек с использованием Git в рамках учебного курса Яндекс.Практикум.


# Стек технологий
<p>
  <a 
  target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-_3.7-green.svg">
  </a>
  <a 
  target="_blank" href="https://www.djangoproject.com/download/" title="Django Framework"><img src="https://img.shields.io/badge/django-2.2-green.svg">
  </a>
  <a 
  target="_blank" href="https://www.django-rest-framework.org/" title="Django REST Framework"><img src="https://img.shields.io/badge/DRF-3.12-green.svg">
  </a>
  <a 
  target="_blank" href="https://django-filter.readthedocs.io/en/stable/" title="Django-filter"><img src="https://img.shields.io/badge/django--filter-21.1-green.svg">
  </a>
  <a 
  target="_blank" href="https://django-rest-framework-simplejwt.readthedocs.io/en/stable/" title="JWT"><img src="https://img.shields.io/badge/DRF--SimpleJWT-5.2-green.svg">
  </a>
</p>

## Установка проекта и зависимостей локально:
Клонируйте проект себе на локальную машину:
```zsh
git clone https://github.com/luydmila-davletova/api_yamdb.git
```
Установите виртуальное окружение:
```zsh
Mac: python3 -m venv venv
Windows: python -m venv venv
```

Активируйте виртуальное окружение:
```zsh
Mac: source venv/bin/activate
Windows: source venv/scripts/activate
```
Обновление pip:

```zsh
python -m pip install --upgrade pip
```

Установите необходимые зависимости:
```zsh
pip install -r requirements.txt
```

Выполните миграции:
```zsh
Mac: python3 manage.py migrate
Windows: python manage.py migrate
```

Для запуска проекта на локальной машине введите:
```zsh
Mac: python3 manage.py runserver
Windows: python manage.py runserver
```

YaMDb будет доступен по адресу:
```zsh
http://127.0.0.1:8000
```
[Примеры запросов и документация](http://127.0.0.1:8000/redoc/)

## Разворачиваем контейнер

### Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```
## Установка Docker на linux:

### Удаляем старый Docker:
```bash
sudo apt remove docker
```

### Устанавливаем Docker:
```bash
sudo apt install docker.io
```
### Активируем Docker в системе:
```bash
sudo systemctl enable docker
```
### Запускаем Docker:
```bash
sudo systemctl start docker
```

### 
Разворачиваем контейнеры: 
    infra_db - база,
    infra_web - веб,
    infra_nginx - nginx сервер
    sudo systemctl stop nginx (останавливаем nginx):
```bash
sudo docker-compose up -d --build 
```

### Выполняем миграции в контейнере infra_web:
```bash
sudo docker-compose exec web python manage.py makemigrations reviews 
```
```bash
sudo docker-compose exec web python manage.py migrate --run-syncdb
```
### Создаем суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser 
```

### Собираем статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input 
```

### Шаблон наполнения .env расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db 
DB_PORT=5432 
```
Разработчики:
```zsh
1. Кирилл Марин (https://github.com/MilkaMjoy):
Разработка системы регистрации и аутентификации, прав доступа, работы с токеном, системы подтверждения через e-mail.

2. Ярослав Мигунов (https://github.com/Migunov-Yaroslav):
Разработка моделей "категории" (Categories), "жанры" (Genres) и "произведения" (Titles), а также разработка представлений и эндпойнтов для них.

3. Людмила Давлетова (https://github.com/luydmila-davletova):
Разработка моделей "отзывы" (Review) и "комментарии" (Comments), а также разработка представлений и эндпойнтов для них. Настройка прав доступа для запросов. Реализация системы рейтингов.
```

