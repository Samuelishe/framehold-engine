# Framehold Engine

Framehold Engine — self-hosted web gallery engine for photo portfolios.

## Что это

Framehold Engine — долгосрочный full-stack проект для собственной фотогалереи с публичным портфолио, ролями авторов и административным управлением контентом.

## Что это не

Это не быстрый статический сайт, не учебный CRUD-демо-CMS и не обвязка вокруг готового галерейного продукта как основной архитектуры.

## Текущий статус

Сейчас проект находится на стадии documentation/bootstrap. На этом этапе зафиксированы цели, требования, архитектурные ориентиры и правила дальнейшей разработки. Django/Wagtail-проект еще не инициализирован.

## Планируемый стек

- Python 3.14
- Django
- Wagtail
- PostgreSQL
- Tailwind CSS
- Alpine.js или HTMX для небольшой интерактивности
- PhotoSwipe или аналогичный lightbox
- Pillow или libvips для обработки изображений
- Docker Compose
- VPS-деплой
- Nginx или Caddy как reverse proxy

## Документация

Основная карта документации: [docs/README.md](/C:/Users/filed/PycharmProjects/framehold-engine/docs/README.md)

## Правила по данным и секретам

В репозиторий нельзя коммитить секреты, `.env`-файлы, дампы БД, приватные ключи, приватные медиафайлы и реальные приватные данные.
