# PROJECT_STATE

## Текущее состояние

- Проект находится на pre-alpha technical foundation stage.
- Django/Wagtail foundation инициализирован.
- Создан `manage.py`, пакет `framehold`, split settings `framehold.settings.base/dev/test/prod`.
- Создан custom User в `apps.accounts`: `accounts.User(AbstractUser)` без `username`, с уникальным нормализованным email как `USERNAME_FIELD`.
- Создан minimal `apps.sitecontent` с Wagtail `HomePage` для корневой страницы.
- Созданы `pyproject.toml`, `uv.lock` и `.python-version`.
- Dependencies установлены через uv; `.venv` остается локальным ignored артефактом.
- Созданы первые миграции `accounts.0001_initial`, `sitecontent.0001_initial`, `sitecontent.0002_create_homepage`.
- Первые миграции выполнены на PostgreSQL 18, не на SQLite.
- Создан database-only `compose.dev.yml` для PostgreSQL `db` service.
- Созданы foundation tests для custom User, django-allauth configuration, Wagtail foundation, PostgreSQL test DB и settings imports.
- Portfolio, Album, Photo, AlbumPhoto, Framehold Dashboard, public portfolio routes, themes, uploads, account deletion, Tailwind/CSS/JS frontend и production containers еще не реализованы.
- Production deployment еще не существует.
- Корневой `README.md` теперь является GitHub landing page на английском языке.

## Принятые продуктовые уточнения

- Framehold Engine теперь определяется как self-hosted multi-user, multi-portfolio web gallery engine.
- Public registration с mandatory email verification является core capability.
- Framehold Dashboard является core product component для Portfolio Owners, а не optional future fallback.
- Curated theme system является defining capability, а не distant future idea.
- Multi-portfolio ownership isolation является hard requirement.
- Лицензия проекта: GNU Affero General Public License version 3 or later, SPDX `AGPL-3.0-or-later`.
- Portfolio и Album приняты как regular Django domain models, не Wagtail Pages.
- Photo принят как Framehold domain model, который initially references the standard Wagtail Image model.
- Custom Wagtail image model не планируется для initial implementation.
- Preferred initial login direction: email-only login; public identity belongs to Portfolio through `slug` and `public_name`.
- One domain `Photo` corresponds to one standard Wagtail Image asset in the MVP; reuse across albums happens through `AlbumPhoto`.
- Private source originals, public full-resolution assets and public renditions are separate architectural concepts.
- Production hosting assumption: Linux VPS, typically Ubuntu or another Debian-like server.
- Repository hygiene now includes `.editorconfig` and `.gitattributes` for stable formatting and LF normalization.
- Account deletion and all data является core product requirement.
- Published photographs are expected to be viewable and saveable; Framehold Engine не является DRM/anti-copy продуктом.
- Default publication approval policy: `none`; moderation is optional and operator-configured.
- Canonical public URL scheme accepted: `/portfolio/<portfolio_slug>/` and `/portfolio/<portfolio_slug>/albums/<album_slug>/`.
- Built-in safe default theme: `minimal_justified`.
- Portfolio main gallery has portfolio-level photo visibility and ordering.
- Owner-authored content is plain text in MVP.
- Captions default visible; capture date and EXIF default hidden.
- No mandatory telemetry, analytics, phone-home behavior, external fonts or public CDN dependency.
- Account deletion uses a two-phase lifecycle: immediate lockout/public removal, then idempotent cleanup.
- MVP vertical slice is documented in `PRODUCT_VISION.md` and `REQUIREMENTS.md`.
- Technical foundation implemented with CPython 3.14.0 in the local environment, Django 5.2.15, Wagtail 7.4.2, django-allauth 65.18.0, django-environ 0.13.0, Psycopg 3.3.4, PostgreSQL image `postgres:18.4-bookworm`, Ruff 0.15.18, pytest 9.1.0, pytest-django 4.12.0 and pytest-cov 7.1.0.
- Dependency management implemented with uv, root `pyproject.toml`, committed `uv.lock`, `.python-version`, project-local `.venv`.
- Accepted direct foundation dependencies: Django, Wagtail, django-allauth, django-environ and `psycopg[binary]`.
- Account foundation uses django-allauth regular accounts with email-plus-password login, mandatory email verification and no `socialaccount` in foundation.
- Custom User contract accepted: `apps.accounts`, `accounts.User(AbstractUser)`, no `username`, unique normalized email as `USERNAME_FIELD`.
- Database direction accepted: PostgreSQL 18 with Psycopg 3; no SQLite fallback in dev/test/production settings.
- Settings split accepted: `framehold.settings.base/dev/test/prod` with django-environ.
- Development Compose implemented as `compose.dev.yml` with PostgreSQL `db` service only; Django runs directly through uv/PyCharm/terminal.
- Development tooling accepted: Ruff, pytest, pytest-django and pytest-cov.
- Initial app boundaries accepted: `apps.accounts` during foundation and `apps.sitecontent` only if required for minimal Wagtail global CMS/root page.
- First migrations must be PostgreSQL-first and after custom User, split settings and database configuration are ready.
- Исходный сценарий Irwyn, Polina и отца Irwyn остается первым intended use case, но не ограничивает продукт.

## Что уже сделано

- Создан корневой README.
- Создан `AGENTS.md` с правилами для будущих агентских сессий.
- Создан базовый комплект документов в `docs/`.
- Добавлен и уточнен `.gitignore` для Python/Django/Wagtail-репозитория, включая исключение локальных артефактов PyCharm.
- Обновлена документация под модель public registration, Portfolio Owner, Framehold Dashboard, curated themes и media presentation.
- Добавлены документы по account deletion/data lifecycle, content rights/media access, open-source/third-party policy и privacy/operator responsibilities.
- Добавлены root `LICENSE`, `THIRD_PARTY_NOTICES.md` и `licenses/README.md`.
- Реализован Stage 1/2 foundation: uv project metadata, dependency lock, Django/Wagtail scaffold, custom User, split settings, PostgreSQL development service, minimal Wagtail site, first migrations and foundation tests.

## Следующие архитектурные вопросы

Перед инициализацией доменной реализации нужно явно решить:

- exact quotas and upload limits;
- exact private-source/public-delivery media storage implementation;
- exact storage cleanup strategy for source originals, public full-resolution assets and renditions.
- decoder/image backend.

- exact production cache backend for allauth rate limits, later.

## Следующий шаг

Следующий шаг: Stage 3 accounts foundation. Следующая задача должна реализовать django-allauth account-flow UX: public registration pages, mandatory email verification flow, login/logout, password reset, account tests and safe redirects. Media spike remains required before real uploads, but does not block accounts foundation.
