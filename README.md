# API Yatube

### Описание проекта:
Благодаря  этому проету можно:
- создавать, редактировать, удалять посты
- подписываться на автора
- создавать, удалять, редактировать комментарии под постами других авторов
- получать список сообществ и подробную информацию о сообществе

### Как установить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Etl0n/api_final_yatube.git
```
```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```
```
source venv/Source/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```
```
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

application/json

[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]

POST http://127.0.0.1:8000/api/v1/follow/

application/json

{
    "following": "string"
}

