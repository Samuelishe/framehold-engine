# DATA_MODEL

## Статус документа

Это черновая модель предметной области. Она описывает планируемые сущности, но не означает, что структура уже реализована.

## User

Используется стандартный пользователь Django/Wagtail.

## PhotographerProfile

Планируемые поля:

- `user`
- `slug`
- `public_name`
- `bio`
- `avatar`
- `cover_photo`
- `sort_order`
- `is_active`

Назначение: публичный профиль фотографа и связка с учетной записью для административной работы.

## Album

Планируемые поля:

- `owner`
- `title`
- `slug`
- `description`
- `cover_photo`
- `status` со значениями `draft`, `published`, `hidden`
- `date_from`
- `date_to`
- `location`
- `created_at`
- `updated_at`
- `sort_order`

Назначение: редакторская единица публикации, объединяющая фотографии в одну публичную историю или подборку.

## Photo

Планируемые поля:

- `album`
- `image`
- `title`
- `description`
- `exif_json`
- `sort_order`
- `uploaded_by`
- `is_cover_candidate`
- `created_at`
- `updated_at`

Назначение: отдельная фотография внутри альбома с порядком, описанием и служебными метаданными.

## SiteSettings

Планируемые поля:

- `site_title`
- `site_subtitle`
- `hero_album`
- `hero_photo`
- `featured_albums`
- `about_text`
- `contact_email`
- `active_theme`

Назначение: глобальная конфигурация публичной части сайта.

## Открытые решения

- Должно ли `Photo.image` ссылаться на Wagtail Image или использовать собственный `ImageField`.
- Должен ли `Album` быть обычной Django-моделью или Wagtail Page.
- Является ли модерация публикации обязательной или опциональной.
- Как именно хранить EXIF: целиком JSON, нормализованные поля, гибридный вариант.
- Как позже вводить теги, коллекции и дополнительные классификаторы.
