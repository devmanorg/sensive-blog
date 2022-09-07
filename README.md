# Блог им. Юрия Григорьевича

Блог о коммерческом успехе Юрия Григорьевича. Делюсь советами по бизнесу, жизни и о воспитании детей.

![Скриншот](screenshots/site.png)

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_FILEPATH` — полный путь к файлу базы данных SQLite, например: `/home/user/schoolbase.sqlite3`
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).

В частности, репозиторий используется:

- В уроке "Оптимизируем сайт" курса [Знакомство с Django: ORM](https://dvmn.org/modules/django-orm/).
- В туториале [Превью для ImageField в админке](https://devman.org/encyclopedia/django/how-to-setup-image-preview/)
