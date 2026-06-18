# Framehold Engine

Framehold Engine — self-hosted multi-user, multi-portfolio web gallery engine for photography portfolios.

## Что это

Framehold Engine — долгосрочный full-stack проект для публикации независимых публичных фотопортфолио в одной self-hosted установке. Пользователь сможет зарегистрироваться, подтвердить email, создать портфолио, выбрать curated theme, загрузить фотографии через приватный Framehold Dashboard, собрать альбомы и опубликовать публичную страницу.

Исходный личный сценарий для Irwyn, Polina и отца Irwyn остается актуальным, но теперь это первые пользователи, а не граница продукта.

## Что это не

Это не социальная сеть, не коммуникационная платформа, не быстрый статический сайт, не generic CMS demo и не обвязка вокруг готового галерейного продукта. В MVP не планируются комментарии посетителей, лайки, подписки, публичная лента активности, личные сообщения, рейтинги, анонимные загрузки и обязательные social sharing buttons.

Текст у фотографии — это авторская подпись или заметка автора, а не visitor comment.

## Текущий статус

Проект находится на стадии documentation/bootstrap и product refinement. Django/Wagtail-проект еще не инициализирован, прикладного кода нет.

## Планируемый стек

- Python 3.14
- Django
- Wagtail
- PostgreSQL
- Tailwind CSS
- Alpine.js или HTMX для небольшой интерактивности
- PhotoSwipe или аналогичный viewer/lightbox
- Pillow или libvips для обработки изображений
- Docker Compose позже
- VPS-деплой позже
- Nginx или Caddy как reverse proxy позже
- SMTP-compatible email delivery в production

## Документация

Основная карта документации: [docs/README.md](/C:/Users/filed/PycharmProjects/framehold-engine/docs/README.md)

## Правила по данным и секретам

В репозиторий нельзя коммитить секреты, `.env`-файлы, дампы БД, приватные ключи, приватные медиафайлы и реальные приватные данные.
