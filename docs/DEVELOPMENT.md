# DEVELOPMENT

## Статус

Stage 1/2 foundation реализован. Этот документ описывает проверенный локальный workflow для текущего pre-alpha состояния.

Точный контракт и результаты Stage 1/2 описаны в `docs/TECHNICAL_FOUNDATION.md`.

## Primary IDE

Основная IDE: JetBrains PyCharm Professional.

Windows remains a valid development environment. Production assumptions are Linux-oriented.

## Local workflow

- uv-managed project-local `.venv` как базовый режим локальной разработки.
- Root `pyproject.toml`, committed `uv.lock` and `.python-version` созданы.
- Application runs directly from PyCharm Professional or terminal through uv.
- `compose.dev.yml` contains PostgreSQL `db` service only.
- Environment variables outside Git.
- Settings split: `framehold.settings.base/dev/test/prod`.
- Custom User model and standard Wagtail Image strategy before first permanent migrations.
- Portfolio and Album are accepted as regular Django domain models.
- Standard Wagtail Image is accepted as the initial image strategy for Framehold Photo.
- Use POSIX-style paths in deployment-oriented documentation and avoid relying on case-insensitive filesystem behavior.
- No SQLite fallback in dev or test settings.
- Do not use Poetry, PDM or parallel requirements files alongside uv.

## Проверенные команды

Подготовить зависимости:

```powershell
uv sync --locked
```

Создать локальный `.env` из safe example:

```powershell
Copy-Item .env.example .env
```

Запустить PostgreSQL 18:

```powershell
docker compose -f compose.dev.yml up -d db
```

Применить миграции:

```powershell
uv run python manage.py migrate
```

Проверить проект:

```powershell
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Запустить development server:

```powershell
uv run python manage.py runserver
```

Остановить PostgreSQL без удаления named volume:

```powershell
docker compose -f compose.dev.yml down
```

## Development email

Для development:

- console email backend initially.

Production credentials must not be used in development and must not be committed.

## Migrations

- Миграции будут штатным Django mechanism.
- First permanent migrations must not be created before custom User, PostgreSQL/dev settings and standard Wagtail Image strategy are ready.
- First migrations run against PostgreSQL, not SQLite.
- `accounts.User` must appear in `apps/accounts/migrations/0001_initial.py`.
- Миграции должны быть reviewable.

## Tests

Accepted tooling: pytest, pytest-django and pytest-cov.

Current pytest direction:

- `DJANGO_SETTINGS_MODULE = "framehold.settings.test"`;
- tests use PostgreSQL test database;
- test filenames use `test_*.py`;
- no mandatory coverage percentage before meaningful application code exists.

Текущие foundation tests покрывают custom User, django-allauth settings, Wagtail homepage/admin, PostgreSQL test DB и settings imports.

Будущие priority tests:

- registration and verification restrictions;
- ownership isolation;
- upload restrictions;
- publication/public filtering;
- suspension behavior;
- theme fallback;
- public EXIF allowlist.
- account deletion lifecycle;
- media access boundaries;
- third-party notice consistency.

## Licensing and third-party workflow

- Future dependencies/assets require provenance and license review.
- Update `THIRD_PARTY_NOTICES.md` when dependencies/assets are included, vendored, adapted, removed or upgraded where relevant.
- Preserve upstream copyright and license headers.
- Do not add unlicensed copied assets.
- Future releases need a license/notice audit.

## Formatting and linting

Accepted tooling: Ruff for formatting and linting.

Ruff direction:

- target Python 3.14;
- line length 100;
- use Ruff formatter;
- begin with focused rule families such as `E`, `F`, `I`, `UP`, `B`;
- do not enable every available lint rule immediately.

Do not add Black, isort, Flake8, pylint, mypy, django-stubs, pre-commit, tox or nox during foundation.

Repository hygiene:

- `.editorconfig` sets UTF-8, LF line endings, final newline and trailing whitespace trimming for repository text files.
- `.gitattributes` normalizes repository text files to LF and marks common binary formats.
- CRLF conversion warnings may appear on Windows depending on Git `autocrlf`; committed content should remain normalized.

## Secrets and data

- No real secrets in repository.
- No `.env` commits.
- No DB dumps in Git.
- No private media in Git.

## Foundation validation

Stage 1/2 validation commands documented in `docs/TECHNICAL_FOUNDATION.md` were run successfully, except production deploy-check intentionally still reports HSTS/HTTPS redirect warnings pending final reverse proxy policy.
