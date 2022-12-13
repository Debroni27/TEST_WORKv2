Запуск базы данных (надо сдлеать в первую очередь)

    docker-compose up db

Зайти в контейнер для конфигурции баз Postgres(при необходимости)

    docker exec -it {id контейнера} psql -U ${USER} ${NAME} bash

Запуск проекта

    docker-compose up web

Загрузить базу тестовыми значениями

    docker-compose up filldb

В результате в базе будут записи  и будет создан суперюзер
Логин: admin
Пароль: adminadmin


Запуск тестов

    docker-compose up test

Запуск линтера (flaske8)

    docker-compose up linter

