# TECH_STACK

## Выбранное направление

### Python 3.14

Планируемая основная версия языка. Совместимость библиотек нужно проверить на этапе инициализации.

### Django

Server-side основа с ORM, migrations, auth, sessions, password hashing, forms and security mechanisms.

### Custom Django User model

Custom User должен существовать с самого начала, до первых permanent application migrations. Точное поле login/email strategy пока открыто.

### Mature registration/email verification package

Нужна established package для registration, mandatory email verification, password reset and related account flows. Точный выбор не сделан. `django-allauth` является кандидатом, но не выбран окончательно.

### Wagtail

Используется для Wagtail Admin, global CMS content, settings and image-related capabilities where appropriate. Self-registered Portfolio Owners не получают Wagtail Admin access автоматически.

### PostgreSQL

Primary DB для development и production.

### Tailwind CSS

Основной styling layer для public pages и Framehold Dashboard.

### Alpine.js или HTMX

Допускаются для небольшой локальной интерактивности без SPA-first архитектуры.

### PhotoSwipe или альтернатива

Планируется как основа common viewer/lightbox behavior. Точный выбор можно подтвердить перед Stage 8.

### Pillow или libvips

Планируются для decoding/validation, renditions/previews and image processing. Exact choice remains open.

### SMTP-compatible email

Production email delivery planned through SMTP-compatible provider. Provider not selected. Credentials must come from environment variables.

### Docker Compose

Планируется позже для environment/deployment, но не создается на documentation stage.

### Nginx или Caddy

Reverse proxy на VPS later.

### Storage

Local VPS filesystem media storage first. S3-compatible storage and Cloudflare R2 are future options, not starting requirements.

## Не выбранные основные пути

- WordPress
- Piwigo
- Lychee
- Immich
- PhotoPrism
- static-only site
- SPA-first frontend
- Next.js
- microservices

## Запреты и ограничения

- Не реализовывать custom auth protocol.
- Не реализовывать custom password hashing.
- Не реализовывать custom session handling.
- Не реализовывать custom token cryptography.
- Не pin dependencies до появления реального проекта и проверки совместимости.
