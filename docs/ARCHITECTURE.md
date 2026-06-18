# ARCHITECTURE

## Базовое направление

- Основа проекта: Django/Wagtail; Stage 1/2 foundation реализован.
- Runtime foundation: CPython 3.14, Django 5.2 LTS, Wagtail 7.4 LTS.
- Dependency management implemented with uv, root `pyproject.toml`, committed `uv.lock`, `.python-version` and project-local `.venv`.
- Custom Django User model создан с самого начала, до первых permanent application migrations.
- Implemented custom User contract: `apps.accounts`, `accounts.User(AbstractUser)`, no `username`, unique normalized email as `USERNAME_FIELD`.
- django-allauth foundation uses `allauth` and `allauth.account` only.
- Portfolio и Album являются regular Django domain models в принятой initial architecture.
- Photo является Framehold domain model and references the standard Wagtail Image model initially.
- One domain Photo corresponds to one Wagtail Image asset in the MVP.
- Custom Wagtail image model is not planned for initial implementation.
- Preferred initial login direction: email-only login.
- Default publication approval policy is `none`; moderation is optional and operator-configured.
- Canonical public routes: `/`, `/portfolios/`, `/portfolio/<portfolio_slug>/`, `/portfolio/<portfolio_slug>/albums/<album_slug>/`, `/accounts/`, `/dashboard/`, `/admin/`.
- Production assumption: Linux VPS, typically Ubuntu or Debian-like server. Windows remains a supported development environment, not the production target.
- Wagtail Admin reserved for Site Administrator and trusted staff.
- Framehold Dashboard — custom Django UI для Portfolio Owners.
- Кастомная доменная логика Portfolio, Album, Photo и AlbumPhoto должна жить в Django apps.
- PostgreSQL 18 — primary DB. Psycopg 3 with `psycopg[binary]` is implemented for foundation.
- No SQLite fallback in dev, test or production settings.
- Public frontend на первом этапе server-rendered.
- Tailwind — основной styling layer.
- Alpine.js или HTMX допускаются только для локальной интерактивности.
- PhotoSwipe или аналогичный viewer/lightbox планируется для media presentation.
- Local filesystem media storage first; S3-compatible storage later.
- Initial development Compose implemented as database-only `compose.dev.yml` with PostgreSQL `db`; production Docker Compose planned later.

## Logical areas

### Framehold Accounts

Custom User and django-allauth foundation configuration are implemented. Public registration UX, email verification flow, login/logout, password reset, onboarding, account states, suspension and deletion remain later stages.

### Framehold Portfolio

Portfolio ownership, Album, Photo, AlbumPhoto, publication state, moderation state, discoverability, presentation defaults, slug/public identity и domain rules.

### Framehold Dashboard

Private custom Django UI for Portfolio Owners. Управляет только текущим Portfolio: uploads, albums, captions, ordering, theme selection и presentation settings.

### Wagtail Admin

Интерфейс Site Administrator и trusted staff для global CMS content, users, system-level data, global settings, themes management и emergency corrections.

### Framehold Theme System

Trusted code-defined curated themes, registry, settings schema, capabilities, responsive contract и fallback behavior.

### Framehold Media Presentation

Responsive renditions/previews, public viewer/lightbox, captions, alt text, dates, controlled EXIF и media delivery policy.

Private source originals, public full-resolution assets and public renditions are separate concepts. Conceptual local filesystem direction: `private_media/sources/`, `public_media/full/`, `public_media/renditions/`.

### Framehold Data Lifecycle

Account deletion, immediate public removal, session revocation, owned-data cleanup, media cleanup, idempotent retry, partial-failure detection and backup/restore interaction.

### Repository Governance

AGPL project license, third-party notices, provenance of included assets, and separation between software license and user-content rights.

### Framehold Public

Theme-driven public pages, safe public querysets and rendered contexts containing only published, non-suspended content.

Public visibility predicates are resolved by application/domain layers before rendering. Themes present prepared data and must not construct unrestricted queries.

### Framehold Config

SiteSettings: registration enabled, publication approval policy, storage quota defaults, global homepage, about/contact data.

### Deployment/Runtime Layer

uv project metadata, split settings, environment variables, PostgreSQL 18 and database-only development Compose are implemented. Containers later, reverse proxy, media volume, production email infrastructure, backups and runtime configuration remain later stages.

## Framehold Dashboard versus Wagtail Admin

Self-registered users must not automatically receive `is_staff`, `is_superuser`, Wagtail Admin access, global Wagtail collection access or page tree permissions.

Framehold Dashboard must remain understandable for non-technical users and must not expose technical Wagtail internals.

Wagtail Admin remains reserved for Site Administrator and explicitly trusted staff.

## Architecture boundaries

- Do not put domain rules only in templates.
- Do not put permissions only in frontend.
- Do not duplicate auth/session/password logic.
- Do not implement custom auth protocol or custom token cryptography.
- Do not enable `allauth.socialaccount`, MFA, headless API, magic-code login, phone auth or JWT flows without separate decision.
- Do not run first migrations before custom User, split settings and PostgreSQL configuration exist.
- Do not use SQLite as temporary migration target.
- Do not let public pages query drafts accidentally.
- Do not let Portfolio Owners edit another portfolio.
- Do not let templates query unrestricted global Photo or Album collections.
- Do not let themes implement publication policy, moderation checks or media authorization.
- Do not hardcode real private data into seed/demo fixtures.
- Do not allow arbitrary user-supplied theme code in MVP.
- Do not render raw EXIF publicly.
- Do not treat a public media directory as authorization.
- Do not rely on unguessable URLs as authorization.
- Do not use fake DRM or copy-protection controls as a security feature.
- Avoid Windows-specific production assumptions, case-insensitive filesystem assumptions and backslash-only paths.
- Do not edit canonical `LICENSE` text or insert third-party notices into it.
- Do not require mandatory telemetry, analytics, phone-home behavior, external fonts or public CDN services.
- Do not add parallel dependency-management systems or manually edit `uv.lock`.
- Do not create production Docker infrastructure during foundation milestone.

## Open implementation decisions

- Exact publication states.
- Exact quotas and upload limits.
- Exact private-source/public-delivery media storage implementation.
- Exact production cache backend for allauth rate limits.

Private-source versus public-delivery storage must be decided before real uploads, preferably through a small technical prototype with standard Wagtail Image, renditions and local filesystem storage. Portfolio/Album as Wagtail Pages and custom Wagtail image model are not part of the accepted initial architecture.
