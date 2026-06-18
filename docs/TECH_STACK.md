# TECH_STACK

## Выбранное направление

### Python 3.14

Accepted runtime: CPython 3.14 series. Metadata uses `requires-python = ">=3.14,<3.15"` and `.python-version` contains `3.14`. Local foundation validation used CPython 3.14.0.

Use latest stable Python 3.14 patch available. Do not use Python 3.15 pre-release, free-threaded CPython baseline, or Python 3.10-3.13 support matrix in initial metadata.

### Django 5.2 LTS

Accepted initial framework branch: Django 5.2 LTS.

Initial constraint direction: `Django>=5.2.15,<5.3`.

Resolved foundation version: Django 5.2.15.

Django provides server-side ORM, migrations, auth, sessions, password hashing, forms and security mechanisms. Do not select Django 6.0 for foundation.

### Custom Django User model

Custom User должен существовать с самого начала, до первых permanent application migrations. Accepted contract: `apps.accounts`, `accounts.User(AbstractUser)`, no `username`, unique normalized `email`, `USERNAME_FIELD = "email"`.

### Standard Wagtail Image initially

Initial implementation uses the standard Wagtail Image model referenced by Framehold `Photo`. Custom Wagtail image model is not planned initially.

### django-allauth regular accounts

Accepted package: `django-allauth>=65.18.0,<66`.

Resolved foundation version: django-allauth 65.18.0.

Use only `allauth` and `allauth.account` in foundation. Do not enable `allauth.socialaccount`, social providers, MFA, headless API, magic-code login, phone auth, WebAuthn or JWT flows without separate decision.

### Wagtail 7.4 LTS

Accepted initial Wagtail branch: Wagtail 7.4 LTS.

Initial constraint direction: `wagtail>=7.4.2,<7.5`. Wagtail 7.4.0 and 7.4.1 are not acceptable for initial foundation.

Resolved foundation version: Wagtail 7.4.2.

Используется для Wagtail Admin, global CMS content, settings and image-related capabilities where appropriate. Self-registered Portfolio Owners не получают Wagtail Admin access автоматически.

### uv dependency management

Accepted and implemented dependency workflow: uv, root `pyproject.toml`, committed `uv.lock`, committed `.python-version`, project-local `.venv`, `[tool.uv] package = false`.

Do not maintain parallel requirements files. Do not use Poetry or PDM alongside uv. Do not manually edit `uv.lock`.

### PostgreSQL 18 and Psycopg 3

Primary DB для development и production: PostgreSQL 18 series. Driver: Psycopg 3 with initial dependency `psycopg[binary]>=3.3.4,<4`.

Resolved foundation versions: PostgreSQL 18.4 via `postgres:18.4-bookworm`, Psycopg 3.3.4 and psycopg-binary 3.3.4.

No SQLite fallback in dev, test or production settings.

### django-environ

Accepted for typed environment-variable access, `DATABASE_URL` parsing, optional local `.env` loading and strict required settings. Initial constraint: `django-environ>=0.13,<0.14`; resolved foundation version: 0.13.0.

### Linux production target

Production hosting is expected to run on Linux in almost all cases, typically Ubuntu or another Debian-like distribution. Windows remains a valid development environment, especially with PyCharm Professional, but production docs and examples should be Linux-oriented.

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

Initial development Compose implemented: `compose.dev.yml` contains PostgreSQL `db` service only. Django runs directly through uv-managed `.venv` for PyCharm/terminal debugging.

Production Docker Compose remains later deployment stage.

### Ruff and pytest

Accepted initial development tooling: Ruff, pytest, pytest-django and pytest-cov. Resolved foundation versions: Ruff 0.15.18, pytest 9.1.0, pytest-django 4.12.0 and pytest-cov 7.1.0.

Do not add Black, isort, Flake8, pylint, mypy, django-stubs, pre-commit, tox or nox during the foundation milestone.

### Nginx или Caddy

Reverse proxy на VPS later.

### Storage

Local VPS filesystem media storage first. S3-compatible storage and Cloudflare R2 are future options, not starting requirements. Exact private-source/public-delivery implementation remains open.

### License

Project license: GNU Affero General Public License version 3 or later, SPDX `AGPL-3.0-or-later`.

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
- Не exact-pin dependency patches in `pyproject.toml`; `uv.lock` records exact resolved versions.
- Не выбирать private/public media storage implementation без отдельного review.
- Не полагаться на case-insensitive filesystem behavior или Windows-specific production assumptions.
- Не добавлять dependencies outside accepted foundation set без отдельного решения.
