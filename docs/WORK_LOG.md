# WORK_LOG

## 2026-06-18

- Создан документационный каркас проекта Framehold Engine.
- Зафиксированы README, агентские правила, архитектурное направление, требования, роли, план развития и индекс файлов.
- Подтверждено, что на этом этапе Django/Wagtail-проект еще не инициализируется и прикладной код не создается.
- Добавлен и вычищен корневой `.gitignore` под Python/Django/Wagtail-проект с акцентом на локальные секреты, кэши, виртуальные окружения, локальные БД, медиа и IDE-local state.
- Из staged-набора исключены локальные файлы `.idea`, чтобы в коммит не попадали привязки PyCharm к конкретному рабочему окружению.
- Обновлена документация под revised product model: public registration, mandatory email verification, multi-portfolio ownership, Framehold Dashboard, curated theme system, media presentation, upload safety и ownership isolation.
- Зафиксированы final architecture decisions: custom User from the beginning, Portfolio/Album as regular Django domain models, Framehold Photo referencing standard Wagtail Image initially, Framehold Dashboard as normal Portfolio Owner interface.
- Добавлены AGPL-3.0-or-later license, English GitHub README, third-party notice policy, public-media/no-DRM policy, user-content rights, account deletion/data lifecycle и operator responsibility documentation.
- Уточнены AGENTS reading rules, добавлен `docs/DECISIONS.md`, зафиксированы email-only login direction, cardinalities/invariants, public-but-unlisted, optional first-publication moderation, theme settings versioning, Linux VPS assumption и repository formatting через `.editorconfig`/`.gitattributes`.
- Добавлен `docs/PRODUCT_PRINCIPLES.md` и выполнен final product consistency pass: trust-by-default publication, canonical URL scheme, default `minimal_justified`, Portfolio main gallery, album cover rules, safe theme rendering, common viewer contract, plain-text owner content, hidden date/EXIF defaults, no telemetry/CDN и two-phase deletion.
- Добавлен `docs/TECHNICAL_FOUNDATION.md` и выполнен technical foundation readiness pass: CPython 3.14, Django 5.2 LTS, Wagtail 7.4 LTS, uv, django-allauth, exact custom User contract, PostgreSQL 18/Psycopg 3, split settings, database-only dev Compose, Ruff/pytest tooling и PostgreSQL-first migration order.
- Реализован Stage 1/2 foundation: создан uv project, `pyproject.toml`, `uv.lock`, `.python-version`, Django/Wagtail scaffold, custom email-only `accounts.User`, django-allauth foundation configuration, split settings, PostgreSQL 18 `compose.dev.yml`, minimal `sitecontent.HomePage`, first migrations, Ruff/pytest tests and updated third-party notices.
