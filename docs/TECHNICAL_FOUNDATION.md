# TECHNICAL_FOUNDATION

## Назначение

Этот документ фиксирует implementation contract для первого Django/Wagtail foundation milestone. `TECH_STACK.md` описывает технологии и причины выбора; этот документ описывает, как именно Stage 1/2 должны быть инициализированы.

Stage 1/2 foundation реализован: созданы `manage.py`, `pyproject.toml`, `uv.lock`, `.python-version`, Django/Wagtail project, `apps.accounts`, `apps.sitecontent`, split settings, initial migrations, `compose.dev.yml`, Ruff/pytest tooling and foundation tests.

Фактическая реализация остается foundation-only: Portfolio, Album, Photo, AlbumPhoto, Framehold Dashboard, public portfolio routes, themes, uploads, account deletion, production Docker infrastructure and media storage implementation не созданы.

## Runtime versions

### Python

Принятый runtime: CPython 3.14 series.

Фактически используется локальный CPython 3.14.0 через uv-managed `.venv`.

`pyproject.toml`:

```toml
requires-python = ">=3.14,<3.15"
```

`.python-version`:

```text
3.14
```

Правила:

- использовать latest stable Python 3.14 patch, доступный в developer environment;
- не использовать Python 3.15 pre-release;
- не использовать free-threaded CPython как baseline runtime;
- не заявлять поддержку Python 3.10-3.13 в initial application metadata;
- Framehold Engine — application, не reusable library с широкой Python support matrix;
- Windows 11 development и Linux production должны разрешаться из одной uv project metadata;
- platform-specific dependencies требуют explicit environment markers, если они понадобятся.

### Django

Принятая ветка: Django 5.2 LTS.

Initial constraint:

```text
Django>=5.2.15,<5.3
```

Resolved version: Django 5.2.15.

Правила:

- при реализации использовать latest available security/bugfix patch из Django 5.2 LTS;
- exact resolved patch фиксируется в `uv.lock`;
- `pyproject.toml` фиксирует accepted minor-series range;
- не выбирать Django 6.0 для initial foundation;
- не использовать development, alpha, beta или release-candidate Django version;
- upgrade Django/Wagtail series — отдельное reviewed change, не casual часть feature work.

Причина: Django 5.2 — LTS, поддерживает Python 3.14, совместим с выбранной Wagtail branch и лучше подходит для long-running learning/product project.

### Wagtail

Принятая ветка: Wagtail 7.4 LTS.

Initial constraint:

```text
wagtail>=7.4.2,<7.5
```

Resolved version: Wagtail 7.4.2.

Правила:

- 7.4.2 — minimum accepted patch из-за важных security fixes;
- при реализации использовать latest compatible 7.4 patch;
- exact resolved version фиксируется в `uv.lock`;
- не использовать Wagtail 7.4.0 или 7.4.1;
- не использовать Wagtail development/pre-release builds;
- Portfolio и Album остаются regular Django domain models;
- standard Wagtail Image остается initial image asset model;
- Wagtail Admin restricted to Site Administrator and trusted staff;
- ordinary self-registered Portfolio Owners используют Framehold Dashboard.

Wagtail initially используется для Wagtail Admin, global CMS content, global operator-managed pages, built-in image/rendition infrastructure, standard Wagtail Image и staff-level system administration.

Wagtail не должен тихо становиться Portfolio Owner dashboard, source of Portfolio ownership, public authorization layer или местом, где Portfolio/Album domain models превращаются в Pages.

## Dependency management with uv

Принято:

- `uv`;
- root `pyproject.toml`;
- committed `uv.lock`;
- committed `.python-version`;
- project-local `.venv`.

Framehold Engine — deployable web application, не Python library для PyPI.

Реализованный uv project direction:

- root `pyproject.toml`;
- `requires-python = ">=3.14,<3.15"`;
- `[project.dependencies]` для direct runtime dependencies;
- `[dependency-groups]` для development/test tools;
- `[tool.uv] package = false`;
- не создавать build backend только ради installable package;
- не использовать uv workspace;
- не создавать несколько pyproject files;
- не поддерживать parallel `requirements/base.txt`, `requirements/dev.txt`, `requirements/prod.txt`;
- не использовать Poetry или PDM рядом с uv;
- не использовать `uv pip install` как обычный project dependency workflow;
- использовать `uv add`, `uv remove`, `uv lock`, `uv sync`, `uv run`;
- `uv.lock` должен быть committed и не редактируется вручную;
- `.venv` остается ignored;
- dependency upgrades — explicit reviewed changes.

Version policy:

- `pyproject.toml` фиксирует accepted direct dependency ranges;
- `uv.lock` фиксирует exact resolved direct и transitive versions;
- security patch upgrades обновляют lockfile;
- не exact-pin every direct dependency в `pyproject.toml`, если policy — minor-series range;
- не использовать unconstrained `*` dependencies.

Future reproducibility commands:

- `uv lock --check`;
- `uv sync --locked`;
- `uv run --locked ...`.

## Direct runtime dependencies

Accepted initial direct runtime dependency set:

- `Django>=5.2.15,<5.3`
- `wagtail>=7.4.2,<7.5`
- `django-allauth>=65.18.0,<66`
- `django-environ>=0.13,<0.14`
- `psycopg[binary]>=3.3.4,<4`

Правила:

- использовать latest compatible patches внутри этих ranges;
- `uv.lock` фиксирует exact versions;
- если official releases advance before implementation, проверить newest compatible patch from official sources;
- не добавлять Django REST Framework, Celery, Redis, Channels, GraphQL, React, Next, Vite, S3 libraries или libvips bindings during foundation;
- не добавлять PhotoSwipe, Tailwind, Alpine.js или HTMX during foundation;
- не добавлять Pillow явно, если он не нужен как direct application dependency на этом этапе; Wagtail may resolve it transitively;
- direct Pillow/media dependencies пересматриваются during media spike.

`django-environ` принят для typed environment-variable access, `DATABASE_URL` parsing, optional local `.env` loading и strict required settings. Custom environment parser не нужен.

Resolved direct runtime dependencies:

- Django 5.2.15
- Wagtail 7.4.2
- django-allauth 65.18.0
- django-environ 0.13.0
- psycopg 3.3.4 with psycopg-binary 3.3.4

Wagtail транзитивно добавил Pillow, djangorestframework and other dependencies; они не являются direct Framehold dependencies.

## django-allauth direction

Принятый package: django-allauth regular account package.

Initial constraint:

```text
django-allauth>=65.18.0,<66
```

Resolved version: django-allauth 65.18.0.

Использовать только:

- `allauth`;
- `allauth.account`.

Не устанавливать и не включать initially:

- `allauth.socialaccount`;
- social login providers;
- MFA app;
- headless API;
- identity-provider functionality;
- phone-number authentication;
- magic-code login;
- WebAuthn;
- JWT token flows.

Причина: Framehold Engine нужны public signup, email-only login, mandatory email verification, password reset, email change verification, account-enumeration protection, rate limits и future reauthentication support.

Не реализовывать custom authentication protocol around django-allauth.

## Accepted django-allauth settings direction

Implemented settings:

```python
ACCOUNT_LOGIN_METHODS = {"email"}

ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "password1*",
    "password2*",
]

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_PREVENT_ENUMERATION = True

ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_CHANGE_EMAIL = True
```

Правила:

- email verification использует link в MVP;
- confirmation требует explicit POST-backed confirmation action, а не incidental GET state change;
- password login остается enabled;
- email-only значит email plus password, не passwordless magic-code login;
- password reset использует verified email;
- email change verifies new address;
- signup собирает только authentication data;
- public name и Portfolio slug собираются during separate onboarding;
- Portfolio onboarding fields не добавляются в django-allauth signup form;
- built-in enumeration protection и rate limits остаются enabled;
- django-allauth token/HMAC mechanisms не заменяются custom cryptography;
- exact email templates и UI styling относятся к accounts implementation stage.

Authentication backends включают Django `ModelBackend` и django-allauth `AuthenticationBackend`.

Required middleware включает `allauth.account.middleware.AccountMiddleware`.

Account routes используют `/accounts/`.

## Rate-limit and client-IP direction

- django-allauth rate limits остаются enabled.
- Не устанавливать `ACCOUNT_RATE_LIMITS = False`.
- Initial implementation начинается с django-allauth defaults.
- Custom limits можно вводить только after tests or observed abuse.
- Rate limiting требует real Django cache backend.
- `DummyCache` запрещен для account flows.
- Development/test may initially use `LocMemCache`.
- Production shared-cache strategy must be finalized before public production registration.
- Redis is not required for MVP.
- Database-backed Django cache may be evaluated as initial shared production option.
- Exact production cache backend remains open until accounts/deployment stage.

Reverse proxy:

- client-IP extraction must not trust arbitrary `X-Forwarded-For`;
- production settings later must match actual Caddy/Nginx topology;
- `ALLAUTH_TRUSTED_PROXY_COUNT` и/или `ALLAUTH_TRUSTED_CLIENT_IP_HEADER` настраиваются только после known reverse proxy design;
- development не должен притворяться, что знает production proxy count;
- Cloudflare-specific assumption не принят.

Это не блокирует foundation initialization.

## Custom User contract

Application: `apps.accounts`.

Model: `accounts.User`.

Base class: `django.contrib.auth.models.AbstractUser`.

Conceptual model shape:

```python
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
```

Добавить custom User manager based on Django standard manager infrastructure.

Manager must support:

- `create_user(email, password=None, **extra_fields)`;
- `create_superuser(email, password=None, **extra_fields)`;
- reject empty email;
- normalize email consistently;
- enforce required superuser flags;
- preserve Django groups and permissions.

Accepted behavior:

- email — only authentication identifier;
- no username field exists;
- `__str__` may return email for staff/admin diagnostics;
- public identity never uses `User.__str__`;
- public identity uses `Portfolio.public_name` and `Portfolio.slug`;
- inherited `first_name` и `last_name` могут остаться для staff/operator identity, но не являются public Portfolio identity;
- avatar, bio, slug, theme, quota, Portfolio settings и presentation fields не принадлежат User;
- ordinary self-registered users default to non-staff and non-superuser;
- `is_active` remains part of Django auth semantics;
- speculative deletion/moderation fields не добавляются в User during foundation;
- future lifecycle state вводится только вместе с workflow.

Email normalization:

- canonical `User.email` storage should be lowercase and trimmed;
- использовать one central normalization path;
- creation и update flows не должны расходиться;
- manager/model/forms/allauth integration must be tested;
- direct QuerySet updates of email that bypass normalization are forbidden;
- `Alice@Example.com` и `alice@example.com` не должны стать двумя active accounts;
- database-level enhancement beyond normalized `unique=True` may be revisited if testing reveals a gap.

Перед first migrations:

```python
AUTH_USER_MODEL = "accounts.User"
```

User model создан в `apps/accounts/migrations/0001_initial.py`.

Не помещать Portfolio или any Portfolio-dependent model в accounts initial migration.

## Custom User and Wagtail compatibility

Foundation validation must verify:

- `createsuperuser` accepts email and password without username;
- superuser can authenticate;
- superuser can access Wagtail Admin;
- Wagtail Admin identifies user meaningfully;
- ordinary User cannot access Wagtail Admin;
- `is_staff=False` remains default for normal users;
- django-allauth resolves custom email field correctly;
- no code imports `django.contrib.auth.models.User` directly;
- relations use `settings.AUTH_USER_MODEL`;
- runtime code uses `get_user_model()` where appropriate.

Не придумывать Wagtail custom-user forms, пока actual foundation test не докажет, что они нужны.

Если Wagtail user creation/edit forms потребуют customization для username-less model, реализовать только minimal supported integration during foundation task и задокументировать это.

## PostgreSQL and Psycopg

Database: PostgreSQL 18 series.

Driver: Psycopg 3.

Initial Python dependency: `psycopg[binary]`.

Правила:

- использовать latest supported PostgreSQL 18 patch in development and later production;
- не target PostgreSQL 19 beta;
- не использовать PostgreSQL 13 или older;
- Django 5.2 application development uses PostgreSQL, not SQLite;
- no silent SQLite fallback in dev, test or production settings;
- tests use PostgreSQL test database created by Django/pytest-django;
- database timezone is UTC;
- database credentials come from environment variables;
- `DATABASE_URL` is canonical connection setting;
- no connection pool in foundation;
- PgBouncer is not part of MVP;
- `psycopg[binary]` selected initially for reliable Windows and Linux development;
- evaluating `psycopg[c]` for later production image remains allowed;
- changing driver variant must not change domain code.

Exact future Docker image tag remains implementation detail, but major series is PostgreSQL 18.

Фактическая development image: `postgres:18.4-bookworm`. Проверенная версия сервера: PostgreSQL 18.4. Volume смонтирован в PostgreSQL 18-compatible path `/var/lib/postgresql`.

## Settings structure

Accepted settings layout:

```text
framehold/
    settings/
        __init__.py
        base.py
        dev.py
        test.py
        prod.py
```

Responsibilities:

`base.py`:

- installed apps;
- middleware;
- templates;
- custom User;
- Wagtail;
- common auth configuration;
- common internationalization/timezone;
- static/media placeholders;
- environment parsing;
- no unsafe development defaults.

`dev.py`:

- `DEBUG=True`;
- localhost hosts/origins;
- console email backend;
- developer-friendly logging;
- local `.env` use;
- PostgreSQL connection;
- no production security pretending.

`test.py`:

- deterministic test settings;
- PostgreSQL test database;
- locmem email backend;
- fast but valid password hasher may be used;
- explicit cache suitable for tests;
- no production services;
- no hidden SQLite.

`prod.py`:

- `DEBUG=False`;
- required `SECRET_KEY`;
- required `ALLOWED_HOSTS`;
- required CSRF trusted origins where needed;
- SMTP configuration;
- HTTPS/security settings later;
- no default development credentials;
- no automatic fallback secret;
- no implicit localhost assumptions.

Rules:

- settings files remain readable;
- no settings-class framework;
- no dynamic settings magic beyond django-environ;
- no broad `try/except` around missing configuration;
- missing required production settings fail fast;
- use pathlib for project paths;
- no Windows-only paths;
- no secrets in source.

`manage.py` default: `framehold.settings.dev`.

Production explicitly sets `DJANGO_SETTINGS_MODULE=framehold.settings.prod`.

Tests explicitly use `framehold.settings.test`.

## Environment configuration

Implemented variables in `.env.example`:

Core:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `FRAMEHOLD_PUBLIC_ORIGIN`

Email:

- `EMAIL_BACKEND`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS`
- `DEFAULT_FROM_EMAIL`

PostgreSQL Compose support may also use:

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`

Rules:

- `.env.example` содержит safe development placeholders only;
- real `.env` remains ignored;
- production may use environment variables или externally mounted secret file supported by deployment;
- OS environment values take precedence over local `.env`;
- no secret defaults in prod;
- booleans/lists/URLs parsed explicitly;
- `FRAMEHOLD_PUBLIC_ORIGIN` is canonical scheme and host for generated account links;
- public origin is not inferred unreliably from arbitrary request headers.

## Development PostgreSQL workflow

Initial local workflow:

- application runs directly through uv-managed `.venv`;
- launched/debugged from PyCharm Professional or terminal;
- database runs in Docker Compose.

Implemented file: `compose.dev.yml`.

Initial Compose scope:

- PostgreSQL `db` service only;
- PostgreSQL 18;
- persistent named volume;
- healthcheck;
- port exposed to localhost for local development;
- credentials from local environment;
- no Django `web` container;
- no reverse proxy;
- no Redis;
- no mail server;
- no object storage;
- no production configuration.

Reason:

- local Django debugging remains simple in PyCharm;
- PostgreSQL behavior matches production direction;
- foundation avoids maintaining duplicate local web runtimes.

Fully containerized web service may be introduced later if it provides real value. Production Docker Compose remains later deployment stage.

## Initial project layout

Implemented root structure:

```text
framehold-engine/
├── manage.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .env.example
├── compose.dev.yml
├── framehold/
│   ├── __init__.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py
│       ├── dev.py
│       ├── test.py
│       └── prod.py
├── apps/
│   ├── __init__.py
│   ├── accounts/
│   └── sitecontent/
├── templates/
├── static/
├── tests/
├── docs/
└── licenses/
```

Initial apps:

1. `apps.accounts`

Created during foundation. Responsibilities: custom User, custom User manager, minimal admin/Wagtail compatibility, future auth/account lifecycle integration.

2. `apps.sitecontent`

Created during foundation for minimal Wagtail root/home-page structure. Responsibilities: operator-managed global CMS content, minimal HomePage, future About/Contact/legal pages.

It must not contain Portfolio, Album, Photo, owner Dashboard logic or account logic.

Later apps, not created during foundation unless explicitly required:

- `apps.portfolios`
- `apps.dashboard`
- `apps.public_site`
- `apps.themes`

Do not create generic dumping-ground apps:

- `core`
- `common`
- `utils`
- `helpers`
- `media`
- `services`

A `services` package may later exist inside focused app when real multi-step workflows exist.

Do not use `src/` layout for this Django application.

## App dependency direction

`accounts`:

- depends on Django auth;
- may integrate with django-allauth;
- must not depend on portfolios.

`sitecontent`:

- depends on Wagtail CMS primitives;
- must not own Portfolio domain logic.

`portfolios`, later:

- depends on `settings.AUTH_USER_MODEL`;
- depends on standard Wagtail Image contracts;
- must not depend on dashboard or public_site.

`dashboard`, later:

- depends on accounts and portfolios;
- contains owner-facing HTTP/UI orchestration;
- does not own domain models.

`public_site`, later:

- depends on portfolios and themes;
- receives safe public view models/DTOs.

`themes`, later:

- presents prepared public data;
- never controls authentication, ownership or visibility.

Rules:

- no circular imports between accounts and portfolios;
- use `settings.AUTH_USER_MODEL` in model fields;
- use `get_user_model()` in runtime code;
- avoid cross-app imports at module import time when stable contract can be used;
- do not create abstraction interfaces before two real implementations exist.

## Wagtail foundation scope

First implementation milestone may create:

- valid Wagtail project;
- Wagtail Admin at `/admin/`;
- minimal operator-managed root/home page;
- standard Wagtail Image support;
- custom User integration;
- static/templates directories required by scaffold.

It must not create:

- Portfolio, Album, Photo, AlbumPhoto models;
- Framehold Dashboard;
- public Portfolio routes;
- themes;
- photo upload workflow;
- custom Wagtail Image model;
- media privacy implementation;
- Tailwind;
- viewer/lightbox;
- production deployment.

Remove unused scaffold/demo code if generated Wagtail template creates features outside foundation scope. Do not preserve placeholder branding or demo pages merely because scaffold generated them.

## Development tooling

Accepted:

- Ruff for formatting and linting;
- pytest for tests;
- pytest-django for Django integration;
- pytest-cov for coverage reporting.

Do not add initially:

- Black;
- isort;
- Flake8;
- pylint;
- mypy;
- django-stubs;
- pre-commit;
- tox;
- nox.

Reason: Ruff covers initial formatting/import/lint needs. pytest-django provides focused Django test support. Static typing infrastructure can be added after real domain code stabilizes. Duplicate formatters/linters create unnecessary conflict.

Development dependency group contains:

- `ruff`
- `pytest`
- `pytest-django`
- `pytest-cov`

Ruff direction:

- target Python 3.14;
- line length 100;
- use Ruff formatter;
- begin with focused rule set;
- do not enable every available lint rule;
- do not silence broad rule categories without explanation;
- per-file ignores are narrow and documented.

Initial useful rule families:

- `E`
- `F`
- `I`
- `UP`
- `B`

Django-specific Ruff rules may be evaluated after Django models exist.

Pytest direction:

- `DJANGO_SETTINGS_MODULE = "framehold.settings.test"`;
- tests must not use SQLite;
- test filenames use `test_*.py`;
- app-specific tests may live under each app;
- cross-app/integration/architecture tests may live in root `tests/`;
- no mandatory coverage percentage before meaningful application code exists;
- coverage threshold may be introduced later.

## First migration order

Mandatory order for next implementation task:

1. Create uv project metadata and resolve dependencies.
2. Scaffold Django/Wagtail project without running migrations.
3. Create `apps.accounts`.
4. Implement custom `accounts.User`.
5. Implement custom User manager.
6. Set `AUTH_USER_MODEL = "accounts.User"`.
7. Configure django-allauth custom-user settings.
8. Configure PostgreSQL and settings split.
9. Start PostgreSQL development service.
10. Run Django system checks.
11. Create `accounts/0001_initial.py`.
12. Review the migration.
13. Create only other minimal foundation migrations genuinely required.
14. Run first migrations against PostgreSQL.
15. Create/test email-based superuser.
16. Test Wagtail Admin access.
17. Run foundation tests and quality checks.

Forbidden ordering:

- do not run `migrate` before custom User exists;
- do not create auth-dependent app migrations before `accounts.User`;
- do not migrate against SQLite and then delete/recreate history for PostgreSQL;
- do not fake migration success by deleting migration files;
- do not squash initial migrations;
- do not add Portfolio models to User migration;
- do not create real user data in migrations.

This order was followed for Stage 1/2. Custom User appears in `apps/accounts/migrations/0001_initial.py`; first migrations were applied to PostgreSQL, not SQLite.

## Planned foundation validation commands

Stage 1/2 validation ran these commands.

Environment/dependencies:

- `python --version`
- `py -3.14 --version`
- `uv --version`
- `uv lock --check`
- `uv sync --locked`
- `uv tree`

Django/Wagtail:

- `uv run python manage.py check`
- `uv run python manage.py check --deploy --settings=framehold.settings.prod`
- `uv run python manage.py makemigrations --check --dry-run`
- `uv run python manage.py showmigrations`
- `uv run python manage.py migrate`
- `uv run python manage.py createsuperuser`
- verify `/admin/` with custom email-based superuser.

Deployment check warnings caused only by intentionally unset production secrets must be reported honestly.

Quality:

- `uv run ruff check .`
- `uv run ruff format --check .`
- `uv run pytest`

Compose:

- `docker compose -f compose.dev.yml config`
- `docker compose -f compose.dev.yml up -d db`
- `docker compose -f compose.dev.yml ps`
- PostgreSQL readiness check;
- `docker compose -f compose.dev.yml down`

Observed production deploy-check warnings remaining after temporary valid environment values:

- `security.W004`: `SECURE_HSTS_SECONDS` intentionally remains unset until final HTTPS/reverse proxy policy.
- `security.W008`: `SECURE_SSL_REDIRECT` intentionally remains unset until final reverse proxy deployment policy.

## Dependency and license governance

Direct dependencies are now installed and locked by uv.

Therefore:

- `THIRD_PARTY_NOTICES.md` now lists verified direct runtime dependencies and development tools;
- do not copy third-party license texts without verified requirement;
- dependency changes must verify direct dependency names, versions, upstream URLs and licenses;
- uv and Ruff are development tools, not Framehold runtime services;
- transitive dependencies remain under their own licenses;
- no proprietary dependency is accepted.

Do not modify canonical `LICENSE`.

## Foundation non-goals

Foundation implementation must exclude:

- Portfolio, Album, Photo, AlbumPhoto;
- SiteSettings domain implementation beyond truly minimal Wagtail requirement;
- onboarding;
- public registration UI implementation;
- custom django-allauth templates;
- Framehold Dashboard;
- public Portfolio pages;
- theme registry;
- Tailwind;
- Alpine.js;
- HTMX;
- PhotoSwipe;
- image upload;
- image sanitization;
- private/public media separation implementation;
- account deletion implementation;
- production Dockerfile;
- production Compose;
- Nginx/Caddy;
- SMTP provider integration;
- S3/R2;
- Redis;
- Celery;
- API framework;
- SPA frontend.

Foundation task provides infrastructure, not a fake half-implemented MVP.
