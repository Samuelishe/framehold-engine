# DECISIONS

Компактный журнал принятых архитектурных решений Framehold Engine. Подробности остаются в topic docs.

## DEC-001 — Custom Django User before initial migrations

- Статус: Accepted.
- Дата или этап: Stage 1.
- Контекст: менять `AUTH_USER_MODEL` после реальных миграций и данных сложно.
- Решение: Framehold Engine использует custom Django User model с самого начала, до первых постоянных application migrations.
- Последствия: custom User должен быть установлен во время Stage 1.
- Supersedes / Superseded by: none.

## DEC-002 — Email-only login as preferred initial direction

- Статус: Accepted as initial direction.
- Дата или этап: Stage 0.6.
- Контекст: публичная identity принадлежит Portfolio, а не authentication credentials.
- Решение: использовать email как login identifier. Не показывать и не требовать public username в MVP. Public identity использует `Portfolio.slug` и `Portfolio.public_name`.
- Последствия: регистрация проще, путаница username/portfolio slug устраняется. Auth package selection later resolved by DEC-022.
- Supersedes / Superseded by: supersedes email plus internal username as equal initial direction.

## DEC-003 — Portfolio and Album are regular Django models

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: public self-service dashboard и ownership scoping являются core requirements.
- Решение: Portfolio и Album являются regular Django domain models, not Wagtail Pages, в принятой initial architecture.
- Последствия: Framehold Dashboard и server-side ownership scoping остаются проще. Wagtail остается полезным для admin/CMS infrastructure, images, settings и global staff workflows.
- Supersedes / Superseded by: supersedes open Page-versus-model decision for initial architecture.

## DEC-004 — Photo references standard Wagtail Image

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: image infrastructure должна переиспользовать Wagtail там, где это полезно, без переноса domain rules в Wagtail Image.
- Решение: Photo является Framehold domain model и initially references the standard Wagtail Image model. Custom Wagtail image model не входит в initial implementation.
- Последствия: Wagtail renditions/focal points/image infrastructure можно переиспользовать. Ownership, captions, EXIF, publication и portfolio-specific rules остаются в Framehold domain models.
- Supersedes / Superseded by: supersedes custom Wagtail image model as initial strategy.

## DEC-005 — One Photo corresponds to one Wagtail Image asset in MVP

- Статус: Accepted for MVP.
- Дата или этап: Stage 0.6.
- Контекст: media lifecycle, ownership и deletion должны оставаться простыми в MVP.
- Решение: domain Photo должен иметь one-to-one relationship with a Wagtail Image asset в MVP. Reuse across albums выполняется через AlbumPhoto, а не через несколько Photo records, указывающих на один Wagtail Image.
- Последствия: упрощаются ownership, deletion, cleanup, EXIF и media lifecycle.
- Supersedes / Superseded by: none.

## DEC-006 — Framehold Dashboard is separate from Wagtail Admin

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: publicly registered Portfolio Owners нужен private non-technical UI.
- Решение: Framehold Dashboard является ordinary private UI для Portfolio Owners. Wagtail Admin зарезервирован для Site Administrator и explicitly trusted staff.
- Последствия: self-registered users никогда не получают Wagtail staff/admin access автоматически.
- Supersedes / Superseded by: supersedes Wagtail Admin as ordinary contributor interface.

## DEC-007 — Published images are saveable; no fake DRM

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: browser-visible images нельзя надежно защитить от копирования.
- Решение: published photographs intentionally viewable/saveable. Public UI uses full-size terminology for public delivery assets and does not imply raw source original exposure. Framehold Engine не использует fake copy protection, context-menu blocking, transparent overlays, canvas-only hiding или DRM.
- Последствия: media security фокусируется на защите unpublished/deleted/suspended content, а не на притворстве, что browser-visible images нельзя скопировать.
- Supersedes / Superseded by: none.

## DEC-008 — Private source and public delivery are separate media concepts

- Статус: Accepted as architectural direction, implementation unresolved.
- Дата или этап: Stage 0.6.
- Контекст: raw uploads могут содержать private metadata и не должны автоматически равняться public assets.
- Решение: различать private source originals, public full-resolution assets и public renditions. Public full-resolution does not imply raw source exposure. Exact storage/delivery implementation остается открытым.
- Последствия: metadata sanitization и draft-media protection нужно спроектировать до real uploads.
- Supersedes / Superseded by: none.

## DEC-009 — Curated themes only in MVP

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: arbitrary user theme code — высокий риск для security и quality.
- Решение: themes являются trusted code-defined presets, shipped with Framehold Engine. Portfolio Owners могут выбирать installed themes и safe settings, но не могут upload arbitrary HTML/CSS/JS/template code в MVP.
- Последствия: улучшаются security и visual quality. User-authored/external themes остаются future-only и требуют separate architecture review.
- Supersedes / Superseded by: none.

## DEC-010 — AGPL-3.0-or-later

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: Framehold Engine — server software, который должен оставаться free and open-source.
- Решение: Framehold Engine licensed under GNU Affero General Public License v3.0 or later.
- Последствия: software license отделен от user-content rights и third-party material licenses.
- Supersedes / Superseded by: none.

## DEC-011 — Linux VPS production assumption

- Статус: Accepted as deployment assumption.
- Дата или этап: Stage 0.6.
- Контекст: production hosting для Django/Wagtail/VPS deployments ожидаемо Linux-oriented.
- Решение: production hosting expected to run on Linux in almost all cases, typically Ubuntu or a similar Debian-like server distribution.
- Последствия: deployment docs, paths, service assumptions, scripts, reverse proxy setup, permissions, backup и runtime examples должны быть Linux-oriented. Windows остается supported development environment, но не main production target.
- Supersedes / Superseded by: none.

## DEC-012 — Trust-by-default publication

- Статус: Accepted.
- Дата или этап: Stage 0.7.
- Контекст: verified Portfolio Owner должен иметь простой путь публикации без ручного review по умолчанию.
- Решение: default publication approval policy is `none`. Optional `first_publication` approval may be enabled explicitly by operator.
- Последствия: verified Portfolio Owners publish independently by default. Suspension remains available to Site Administrator.
- Supersedes / Superseded by: supersedes first-publication approval as default policy.

## DEC-013 — Canonical public URL scheme

- Статус: Accepted.
- Дата или этап: Stage 0.7.
- Контекст: public identity должна быть стабильной и отделенной от authentication credentials.
- Решение: use `/portfolio/<slug>/` for Portfolio and `/portfolio/<slug>/albums/<album-slug>/` for Album. `/portfolios/` is listed directory.
- Последствия: public identity stays separate from authentication credentials and system route conflicts are reduced.
- Supersedes / Superseded by: supersedes open URL scheme decision.

## DEC-014 — Built-in default theme

- Статус: Accepted.
- Дата или этап: Stage 0.7.
- Контекст: onboarding не должен блокироваться выбором темы.
- Решение: `minimal_justified` is non-removable safe default and fallback theme. Theme selection does not block onboarding.
- Последствия: every Portfolio can render even with missing/invalid theme configuration.
- Supersedes / Superseded by: supersedes mandatory initial theme selection during onboarding.

## DEC-015 — Portfolio main gallery composition

- Статус: Accepted.
- Дата или этап: Stage 0.7.
- Контекст: Portfolio page должна поддерживать фотографии без обязательной привязки к Album.
- Решение: Photo may appear directly in Portfolio gallery using portfolio-level visibility and ordering, independently of Album membership.
- Последствия: Albums remain optional organizational/presentation entities. Album ordering remains separate through AlbumPhoto.
- Supersedes / Superseded by: none.

## DEC-016 — Plain-text Portfolio Owner content

- Статус: Accepted for MVP.
- Дата или этап: Stage 0.7.
- Контекст: owner-authored rich text increases XSS and theme consistency risks.
- Решение: Portfolio Owner-authored biography, descriptions, captions, titles, locations and alt text are plain text with template autoescaping.
- Последствия: owner-supplied HTML/Markdown/rich text is not supported in MVP, reducing XSS and theme inconsistency.
- Supersedes / Superseded by: none.

## DEC-017 — Metadata presentation defaults

- Статус: Accepted.
- Дата или этап: Stage 0.7.
- Контекст: automatically extracted metadata can expose private information.
- Решение: captions default visible; capture date and EXIF default hidden. Per-Photo inherit/show/hide overrides may be supported.
- Последствия: automatically extracted metadata is not published without owner intent.
- Supersedes / Superseded by: supersedes earlier ambiguous EXIF default wording.

## DEC-018 — No mandatory telemetry or external asset services

- Статус: Accepted.
- Дата или этап: Stage 0.7.
- Контекст: self-hosted instances should remain independent and privacy-friendly by default.
- Решение: core Framehold Engine and built-in themes do not require telemetry, analytics, project phone-home services, external fonts or public CDNs.
- Последствия: ordinary gallery operation does not depend on project infrastructure or third-party tracking services.
- Supersedes / Superseded by: none.

## DEC-019 — Two-phase account deletion

- Статус: Accepted as lifecycle architecture.
- Дата или этап: Stage 0.7.
- Контекст: deletion must immediately remove public access while preserving enough ownership information for safe cleanup.
- Решение: deletion first blocks access and removes public visibility, then an idempotent cleanup service removes media, domain data, account records and finally active User identity.
- Последствия: partial file failures remain retryable without restoring public access or losing ownership information prematurely.
- Supersedes / Superseded by: supersedes one-step deletion as conceptual model.

## DEC-020 — Python, Django, and Wagtail baseline

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: foundation implementation needs exact supported runtime/framework series before dependency metadata exists.
- Решение: use CPython 3.14, Django 5.2 LTS and Wagtail 7.4 LTS. Initial dependency bounds are Python `>=3.14,<3.15`, Django `>=5.2.15,<5.3`, and Wagtail `>=7.4.2,<7.5`.
- Последствия: project follows supported LTS series and locks exact patches through `uv.lock`. Framework-series upgrades require separate review.
- Supersedes / Superseded by: supersedes broad/unresolved framework version direction.

## DEC-021 — uv project and dependency management

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: foundation needs one reproducible dependency workflow across Windows development and Linux production.
- Решение: use uv with root `pyproject.toml`, committed `uv.lock`, committed `.python-version`, project-local `.venv`, and `[tool.uv] package = false`.
- Последствия: do not maintain parallel requirements files or use Poetry/PDM. `uv.lock` is machine-managed and exact dependency resolution is reproducible.
- Supersedes / Superseded by: supersedes open dependency-management decision.

## DEC-022 — django-allauth for account flows

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: Framehold Engine needs mature signup, verification, reset, email change, enumeration protection and rate-limit behavior.
- Решение: use django-allauth regular accounts for signup, mandatory email verification, email-only login, password reset, email change, enumeration protection, rate limits and future reauthentication.
- Последствия: do not implement custom auth protocol. Social login, MFA, headless API, phone login and magic-code login are excluded from initial implementation.
- Supersedes / Superseded by: supersedes auth package as open candidate decision.

## DEC-023 — Exact initial custom User contract

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: `AUTH_USER_MODEL` must be fixed before first migrations.
- Решение: use `accounts.User(AbstractUser)` without a username field, with unique normalized email as `USERNAME_FIELD` and a minimal custom manager.
- Последствия: `AUTH_USER_MODEL` must be configured before first migration. Public identity remains in Portfolio. User remains focused on authentication and staff capabilities.
- Supersedes / Superseded by: supersedes open custom User base decision.

## DEC-024 — PostgreSQL 18 and Psycopg 3

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: development and production should share PostgreSQL behavior from the first real migrations.
- Решение: use PostgreSQL 18 as development/production database direction and Psycopg 3 with binary extra initially.
- Последствия: no SQLite fallback in development or tests. Production driver variant may be reviewed later without changing domain code.
- Supersedes / Superseded by: supersedes generic PostgreSQL direction without version/driver.

## DEC-025 — django-environ and split settings

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: settings need explicit dev/test/prod behavior and typed environment parsing without custom framework.
- Решение: use django-environ for typed environment configuration and split settings into `base/dev/test/prod`.
- Последствия: required production settings fail fast. Real secrets remain external. Do not create custom settings framework.
- Supersedes / Superseded by: none.

## DEC-026 — Initial Django application boundaries

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: foundation should not create speculative empty apps or domain placeholders.
- Решение: create accounts during foundation and sitecontent only for minimal Wagtail global CMS needs. Add portfolios, dashboard, public_site and themes only in their implementation stages.
- Последствия: avoid empty apps and generic dumping-ground packages. Dependency direction remains explicit.
- Supersedes / Superseded by: none.

## DEC-027 — Ruff and pytest development tooling

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: first toolchain should be small and deterministic.
- Решение: use Ruff, pytest, pytest-django and pytest-cov as initial quality tooling. Defer mypy, django-stubs, pre-commit, tox and duplicate formatters.
- Последствия: formatting, linting and Django tests have one initial path without overlapping tools.
- Supersedes / Superseded by: supersedes formatting/linting tools as open decision.

## DEC-028 — PostgreSQL-first initial migrations

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: custom User and database assumptions must be established before permanent migration history.
- Решение: do not run permanent migrations before custom User, split settings and PostgreSQL development configuration are complete.
- Последствия: first accounts migration contains custom User. SQLite is not used as temporary migration target.
- Supersedes / Superseded by: none.

## DEC-029 — Database-only development Compose

- Статус: Accepted.
- Дата или этап: Stage 0.8.
- Контекст: local Django debugging should remain simple while still using PostgreSQL behavior.
- Решение: initial `compose.dev.yml` contains PostgreSQL only; Django runs directly through uv environment for PyCharm/terminal debugging.
- Последствия: no duplicate local web runtime, reverse proxy, Redis or production container is introduced during foundation.
- Supersedes / Superseded by: none.
