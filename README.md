# API Yatube

### Описание проекта:
---
Благодаря  этому проету можно:
- создавать, редактировать, удалять посты
- подписываться на автора
- создавать, удалять, редактировать комментарии под постами других авторов
- получать список сообществ и подробную информацию о сообществе

Пользоваться полным функционалом может только авторизированный пользователь

### Технологии, которые использовались:
---
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-464646?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/JWT-464646?style=flat-square&logo=JSON%20web%20tokens)](https://jwt.io/)
[![SQLite](https://img.shields.io/badge/sqlite-464646?style=flat-square&logo=sqlite)](https://www.sqlite.org/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

### Как установить проект:
---
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Etl0n/api_final_yatube.git

cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env

source venv/Source/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов
GET http://127.0.0.1:8000/api/v1/groups/
```
application/json
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```
POST http://127.0.0.1:8000/api/v1/follow/
```
application/json

{
    "following": "string"
}
```
## Автор:
[Etl0n](https://github.com/Etl0n) (Ученик Яндекс Практикума)