# FILE_INDEX

## Корень репозитория

- `README.md` — краткое описание Framehold Engine как self-hosted multi-user, multi-portfolio gallery engine.
- `AGENTS.md` — правила для будущих агентских и Codex-сессий.
- `.gitignore` — правила исключения локальных артефактов, секретов, медиа, кэшей и IDE-local state из Git.
- `.editorconfig` — базовые правила кодировки, LF line endings, final newline и indentation для редакторов.
- `.gitattributes` — Git normalization rules для LF line endings и binary assets.
- `LICENSE` — canonical GNU Affero General Public License version 3 text for Framehold Engine.
- `THIRD_PARTY_NOTICES.md` — human-readable inventory and attribution source for included/adapted third-party components and assets.
- `licenses/README.md` — пояснение назначения каталога для будущих third-party license texts.
- `.python-version` — uv/Python version pin for CPython 3.14.
- `.env.example` — safe development environment-variable template.
- `pyproject.toml` — uv project metadata, direct dependencies, Ruff and pytest configuration.
- `uv.lock` — machine-generated uv dependency lockfile.
- `manage.py` — Django management entry point using `framehold.settings.dev` by default.
- `compose.dev.yml` — database-only development Compose file for PostgreSQL 18.

## Django/Wagtail foundation

- `framehold/__init__.py` — package marker for the Django project.
- `framehold/asgi.py` — ASGI entry point.
- `framehold/wsgi.py` — WSGI entry point.
- `framehold/urls.py` — foundation URL routing for Wagtail Admin, Wagtail documents, django-allauth accounts and Wagtail public pages.
- `framehold/settings/__init__.py` — package marker for split settings.
- `framehold/settings/base.py` — common Django/Wagtail/allauth/settings foundation.
- `framehold/settings/dev.py` — development settings.
- `framehold/settings/test.py` — pytest/Django test settings using PostgreSQL.
- `framehold/settings/prod.py` — fail-fast production settings skeleton.
- `apps/__init__.py` — package marker for project apps.
- `apps/accounts/__init__.py` — package marker for accounts app.
- `apps/accounts/apps.py` — Django app config for `accounts`.
- `apps/accounts/managers.py` — custom User manager with email normalization.
- `apps/accounts/models.py` — custom `accounts.User` without username.
- `apps/accounts/display.py` — django-allauth user display helper.
- `apps/accounts/admin.py` — minimal Django admin integration for custom User.
- `apps/accounts/migrations/__init__.py` — accounts migrations package marker.
- `apps/accounts/migrations/0001_initial.py` — first custom User migration.
- `apps/accounts/tests/__init__.py` — accounts tests package marker.
- `apps/accounts/tests/test_user_model.py` — custom User and manager tests.
- `apps/accounts/tests/test_allauth_configuration.py` — django-allauth foundation configuration tests.
- `apps/sitecontent/__init__.py` — package marker for minimal Wagtail global content app.
- `apps/sitecontent/apps.py` — Django app config for `sitecontent`.
- `apps/sitecontent/models.py` — minimal Wagtail `HomePage`.
- `apps/sitecontent/migrations/__init__.py` — sitecontent migrations package marker.
- `apps/sitecontent/migrations/0001_initial.py` — initial `HomePage` model migration.
- `apps/sitecontent/migrations/0002_create_homepage.py` — migration creating the default Wagtail homepage and Site.
- `apps/sitecontent/templates/sitecontent/home_page.html` — minimal homepage template.
- `apps/sitecontent/tests/__init__.py` — sitecontent tests package marker.
- `apps/sitecontent/tests/test_wagtail_foundation.py` — Wagtail homepage/admin access tests.
- `templates/base.html` — minimal base HTML template without external assets.
- `static/.gitkeep` — keeps the empty static directory in Git.
- `tests/__init__.py` — root tests package marker.
- `tests/test_database_settings.py` — verifies PostgreSQL is used in tests.
- `tests/test_settings_imports.py` — verifies settings import behavior and production fail-fast secret handling.

## Каталог docs

- `docs/README.md` — карта документации.
- `docs/PROJECT_STATE.md` — текущее состояние проекта и следующие архитектурные вопросы.
- `docs/PRODUCT_VISION.md` — продуктовая цель, роли, non-social positioning и первые пользователи.
- `docs/PRODUCT_PRINCIPLES.md` — принципы принятия продуктовых и архитектурных решений.
- `docs/REQUIREMENTS.md` — требования к регистрации, dashboard, ownership, темам, media и MVP.
- `docs/ARCHITECTURE.md` — архитектурные области, границы Dashboard/Admin и открытые решения.
- `docs/DECISIONS.md` — компактный журнал принятых архитектурных решений.
- `docs/DATA_MODEL.md` — концептуальная модель User, Portfolio, Album, Photo, AlbumPhoto и SiteSettings.
- `docs/PERMISSIONS.md` — роли Site Administrator, Portfolio Owner, Public Visitor и ограничения доступа.
- `docs/REGISTRATION_AND_ACCOUNTS.md` — регистрация, email verification, account lifecycle, onboarding и auth decisions.
- `docs/OWNERSHIP_AND_ISOLATION.md` — ownership invariants, server-side scoping и future permission tests.
- `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md` — self-service account deletion, cleanup scope, idempotency, backups, restore and future tests.
- `docs/PUBLIC_SITE.md` — theme-driven public pages, URL options, public viewer и filtering rules.
- `docs/ADMIN_WORKFLOW.md` — разделение Framehold Dashboard и Wagtail Admin, onboarding и content flow.
- `docs/THEME_SYSTEM.md` — curated themes, registry, settings schema, responsive contract и initial theme families.
- `docs/MEDIA_PRESENTATION.md` — captions, dates, EXIF, viewer/lightbox, renditions и upload safety.
- `docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md` — no-DRM policy, public media access, source/public/rendition distinction and user-content rights.
- `docs/OPEN_SOURCE_AND_THIRD_PARTY_POLICY.md` — AGPL, third-party policy, asset licensing and release audit direction.
- `docs/PRIVACY_AND_OPERATOR_RESPONSIBILITIES.md` — software versus deployed instance responsibilities and planned legal/configurable pages.
- `docs/UI_DESIGN.md` — визуальное направление, responsive rules, theme families и viewer behavior.
- `docs/TECH_STACK.md` — selected stack, custom User, django-allauth, uv, PostgreSQL и production email direction.
- `docs/TECHNICAL_FOUNDATION.md` — implementation contract для Stage 1/2: runtime versions, uv, dependencies, custom User, settings, PostgreSQL, tooling и migration order.
- `docs/DEVELOPMENT.md` — planned local development, email backend/mail-catcher и migration constraints.
- `docs/DEPLOYMENT.md` — planned VPS deployment, production email, public origin, quotas and backups.
- `docs/SECURITY_NOTES.md` — security rules for registration, verification, ownership, uploads, EXIF and themes.
- `docs/ROADMAP.md` — dependency-aware roadmap.
- `docs/WORK_LOG.md` — журнал заметных шагов.
- `docs/CODING_RULES.md` — правила будущей реализации.
- `docs/FILE_INDEX.md` — индекс созданных файлов и их назначения.
- `docs/FUTURE_IDEAS.md` — отложенные идеи и future-only capabilities.
- `docs/CHANGELOG.md` — пользовательский changelog проекта.
- `docs/archive/work-log/.gitkeep` — служебный файл для сохранения архивного каталога.
