# ARCHITECTURE

## Базовое направление

- Основа проекта: Django/Wagtail.
- Custom Django User model должен быть создан с самого начала, до первых permanent application migrations.
- Wagtail Admin reserved for Site Administrator and trusted staff.
- Framehold Dashboard — custom Django UI для Portfolio Owners.
- Кастомная доменная логика Portfolio, Album, Photo и AlbumPhoto должна жить в Django apps.
- PostgreSQL — primary DB.
- Public frontend на первом этапе server-rendered.
- Tailwind — основной styling layer.
- Alpine.js или HTMX допускаются только для локальной интерактивности.
- PhotoSwipe или аналогичный viewer/lightbox планируется для media presentation.
- Local filesystem media storage first; S3-compatible storage later.
- Docker Compose planned later.

## Logical areas

### Framehold Accounts

Custom User, public registration, email verification, login/logout, password reset, onboarding, account states and suspension.

### Framehold Portfolio

Portfolio ownership, Album, Photo, AlbumPhoto, publication states, presentation defaults, slug/public identity и domain rules.

### Framehold Dashboard

Private custom Django UI for Portfolio Owners. Управляет только текущим Portfolio: uploads, albums, captions, ordering, theme selection и presentation settings.

### Wagtail Admin

Интерфейс Site Administrator и trusted staff для global CMS content, users, system-level data, global settings, themes management и emergency corrections.

### Framehold Theme System

Trusted code-defined curated themes, registry, settings schema, capabilities, responsive contract и fallback behavior.

### Framehold Media Presentation

Responsive renditions/previews, public viewer/lightbox, captions, alt text, dates, controlled EXIF и original media policy.

### Framehold Public

Theme-driven public pages, safe public querysets and rendered contexts containing only published, non-suspended content.

### Framehold Config

SiteSettings: registration enabled, publication approval policy, storage quota defaults, global homepage, about/contact data.

### Deployment/Runtime Layer

Containers later, reverse proxy, environment variables, PostgreSQL, media volume, email infrastructure, backups and runtime configuration.

## Framehold Dashboard versus Wagtail Admin

Self-registered users must not automatically receive `is_staff`, `is_superuser`, Wagtail Admin access, global Wagtail collection access or page tree permissions.

Framehold Dashboard must remain understandable for non-technical users and must not expose technical Wagtail internals.

Wagtail Admin remains reserved for Site Administrator and explicitly trusted staff.

## Architecture boundaries

- Do not put domain rules only in templates.
- Do not put permissions only in frontend.
- Do not duplicate auth/session/password logic.
- Do not implement custom auth protocol or custom token cryptography.
- Do not let public pages query drafts accidentally.
- Do not let Portfolio Owners edit another portfolio.
- Do not let templates query unrestricted global Photo or Album collections.
- Do not hardcode real private data into seed/demo fixtures.
- Do not allow arbitrary user-supplied theme code in MVP.
- Do not render raw EXIF publicly.

## Open implementation decisions

- Portfolio and Album representation: regular Django models, Wagtail Page models or hybrid approach.
- Image representation: default Wagtail Image plus Framehold Photo model, custom Wagtail image model or controlled image asset model.
- Exact publication states.
- Whether first public publication requires Site Administrator approval.
- Canonical public URL scheme.

These decisions must be reviewed before domain implementation and before permanent migration history is established.
