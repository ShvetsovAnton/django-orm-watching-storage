# Терминал для охранника

[![imageup.ru](https://imageup.ru/img13/4126752/chrome_caes5i74ft.jpg)](https://imageup.ru/img13/4126752/chrome_caes5i74ft.jpg.html)
## О проекте: 

Django проект

Помогает получать охраннику следующую информацию:
- активные пропуски
- кто находиться в хранилище
- время пребывания в хранилище
- был ли визит "подозрительным"

[![imageup.ru](https://imageup.ru/img162/4126723/bandicam-2022-12-21-13-32-40-777-online-video-cuttercom-1.gif)](https://imageup.ru/img162/4126723/bandicam-2022-12-21-13-32-40-777-online-video-cuttercom-1.gif.html)

## Как подготовить проект к запуску

Для этого перейдите на сайт [dvmn.org](https://dvmn.org/modules/django-orm/lesson/watching-storage/#1)

В первом уроке будут доступны данные для подключения к тестовой базе

[![imageup.ru](https://imageup.ru/img51/4126717/chrome_bae1b7n6bv.png)](https://imageup.ru/img51/4126717/chrome_bae1b7n6bv.png.html)

1. Создать файл `.env`
2. Положите в корневую папку проекта
3. Данные из урока прописать в файле `.env`

Заполнение полей в `.env`:

 ```python
DJANGO_DB_ENGINE="django.db.backends.postgresql_psycopg2"
DJANGO_DB_HOST="ссылка на базу"
DJANGO_DB_PORT="номер порта"
DJANGO_DB_NAME="имя базы"
DJANGO_DB_USER="имя пользователя"
DJANGO_DB_PASSWORD="пароль"
```
## Как запустить скрипт

```python
python manage.py runserver
```

Сайт будет доступен по локальному адресу - http://127.0.0.1:8000/

## Требования к окружению

Python3 должен быть уже установлен.
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```