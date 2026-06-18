# Документация Framehold Engine

Этот каталог содержит рабочую документацию проекта. На текущем этапе она остается главным источником решений; Stage 1/2 technical foundation уже реализован, а продуктовая доменная реализация еще не начата.

- `PROJECT_STATE.md` — текущее состояние проекта, что реализовано, что только запланировано и какие архитектурные вопросы нужно решить следующими.
- `PRODUCT_VISION.md` — продуктовая рамка: multi-user, multi-portfolio engine, premium portfolio presentation и явные social non-goals.
- `PRODUCT_PRINCIPLES.md` — принципы принятия продуктовых и архитектурных решений.
- `REQUIREMENTS.md` — функциональные и нефункциональные требования, включая регистрацию, dashboard, ownership, темы, media viewer и upload safety.
- `ARCHITECTURE.md` — архитектурное направление, логические зоны системы, границы Framehold Dashboard и Wagtail Admin.
- `DECISIONS.md` — компактный журнал принятых архитектурных решений.
- `DATA_MODEL.md` — концептуальная модель User, Portfolio, Album, Photo, AlbumPhoto и SiteSettings с cardinalities и invariants.
- `PERMISSIONS.md` — роли Site Administrator, Portfolio Owner и Public Visitor, account states и suspension rules.
- `REGISTRATION_AND_ACCOUNTS.md` — registration flow, email verification, account lifecycle, password reset, onboarding и django-allauth direction.
- `OWNERSHIP_AND_ISOLATION.md` — portfolio ownership invariants, server-side scoping, direct object access protection и future permission tests.
- `ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md` — self-service Delete account and all data, cleanup scope, idempotency, backups, restore behavior and future tests.
- `PUBLIC_SITE.md` — theme-driven публичные страницы, URL options, public viewer и правила выдачи только опубликованного non-suspended контента.
- `ADMIN_WORKFLOW.md` — разделение Wagtail Admin и Framehold Dashboard, onboarding и owner content-management flow.
- `THEME_SYSTEM.md` — trusted curated themes, theme registry, settings schema, responsive contract, fallback behavior и initial theme families.
- `MEDIA_PRESENTATION.md` — captions, dates, alt text, controlled EXIF, responsive renditions, viewer/lightbox и upload/media policy.
- `CONTENT_RIGHTS_AND_MEDIA_ACCESS.md` — no-DRM policy, source original/public asset/rendition distinction, user-content rights and public-media access.
- `OPEN_SOURCE_AND_THIRD_PARTY_POLICY.md` — AGPL decision, third-party attribution, asset licensing, license compatibility and repository governance.
- `PRIVACY_AND_OPERATOR_RESPONSIBILITIES.md` — distinction between software project, deployed instance, operator, Portfolio Owners and Public Visitors.
- `UI_DESIGN.md` — визуальное направление публичного интерфейса, mobile rules, theme families и viewer UX.
- `TECH_STACK.md` — выбранный стек, custom User model с начала, planned email infrastructure и невыбранные альтернативы.
- `TECHNICAL_FOUNDATION.md` — точный контракт Stage 1/2: версии, uv, dependencies, custom User, settings, PostgreSQL, migrations и validation commands.
- `DEVELOPMENT.md` — проверенный локальный foundation workflow, PostgreSQL через Compose, uv/Ruff/pytest команды и ограничения текущей реализации.
- `DEPLOYMENT.md` — планируемый VPS deployment, production email, public origin, quotas и backup assumptions.
- `SECURITY_NOTES.md` — правила безопасности для registration, verification, ownership, upload safety, EXIF и suspension.
- `ROADMAP.md` — dependency-aware roadmap от documentation refinement до accounts, dashboard, themes, media и deployment.
- `WORK_LOG.md` — журнал заметных шагов по проекту.
- `CODING_RULES.md` — будущие правила кодирования для Django/Wagtail, ownership scoping, auth, themes и EXIF.
- `FILE_INDEX.md` — индекс файлов документационного каркаса и их назначения.
- `FUTURE_IDEAS.md` — отложенные идеи, не входящие в ранние этапы.
- `CHANGELOG.md` — пользовательский changelog по крупным вехам проекта.
- `archive/work-log/.gitkeep` — служебный файл для сохранения структуры архивного каталога журнала.
