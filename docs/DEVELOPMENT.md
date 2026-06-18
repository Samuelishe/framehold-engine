# DEVELOPMENT

## Статус

Документ описывает planned local development approach. Финальных команд нет, потому что Django/Wagtail project еще не создан.

## Primary IDE

Основная IDE: JetBrains PyCharm Professional.

Windows remains a valid development environment. Production assumptions are Linux-oriented.

## Planned local workflow

- Python virtual environment как базовый режим локальной разработки.
- Docker Compose workflow later, после появления реального проекта.
- Environment variables outside Git.
- Settings split after project initialization.
- Custom User model and standard Wagtail Image strategy before first permanent migrations.
- Portfolio and Album are accepted as regular Django domain models.
- Standard Wagtail Image is accepted as the initial image strategy for Framehold Photo.
- Use POSIX-style paths in deployment-oriented documentation and avoid relying on case-insensitive filesystem behavior.

## Development email

Для development planned:

- console email backend; или
- local mail-catcher.

Production credentials must not be used in development and must not be committed.

## Migrations

- Миграции будут штатным Django mechanism.
- First permanent migrations must not be created before custom User, PostgreSQL/dev settings and standard Wagtail Image strategy are ready.
- Миграции должны быть reviewable.

## Tests

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

Exact formatting/linting tools remain open. Решение будет принято после инициализации проекта.

Repository hygiene:

- `.editorconfig` sets UTF-8, LF line endings, final newline and trailing whitespace trimming for repository text files.
- `.gitattributes` normalizes repository text files to LF and marks common binary formats.
- CRLF conversion warnings may appear on Windows depending on Git `autocrlf`; committed content should remain normalized.

## Secrets and data

- No real secrets in repository.
- No `.env` commits.
- No DB dumps in Git.
- No private media in Git.
