# DEVELOPMENT

## Статус

Документ описывает planned local development approach. Финальных команд нет, потому что Django/Wagtail project еще не создан.

## Primary IDE

Основная IDE: JetBrains PyCharm Professional.

## Planned local workflow

- Python virtual environment как базовый режим локальной разработки.
- Docker Compose workflow later, после появления реального проекта.
- Environment variables outside Git.
- Settings split after project initialization.
- Custom User model and image-model strategy review before first permanent migrations.

## Development email

Для development planned:

- console email backend; или
- local mail-catcher.

Production credentials must not be used in development and must not be committed.

## Migrations

- Миграции будут штатным Django mechanism.
- First permanent migrations must not be created before custom User and image-model strategy are reviewed.
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

## Formatting and linting

Exact formatting/linting tools remain open. Решение будет принято после инициализации проекта.

## Secrets and data

- No real secrets in repository.
- No `.env` commits.
- No DB dumps in Git.
- No private media in Git.
