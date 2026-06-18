# AGENTS.md

## Язык и стиль

- Отвечать пользователю на русском языке.
- Комментарии и docstring в коде писать на русском языке там, где это действительно полезно.
- Корневой `README.md` должен оставаться на английском языке как GitHub landing page.
- Внутренние документы в `docs/` и отчеты Codex пользователю писать на русском языке. Technical identifiers and established technology names may remain in English.

## Базовое чтение перед работой

Перед любой осмысленной работой всегда читать:

- `docs/PROJECT_STATE.md`
- `docs/PRODUCT_VISION.md`
- `docs/PRODUCT_PRINCIPLES.md`
- `docs/ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/CODING_RULES.md`
- `docs/FILE_INDEX.md`
- `docs/DECISIONS.md`

## Task-specific чтение

Для accounts/auth/registration задач дополнительно читать:

- `docs/REGISTRATION_AND_ACCOUNTS.md`
- `docs/PERMISSIONS.md`
- `docs/OWNERSHIP_AND_ISOLATION.md`
- `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md`
- `docs/SECURITY_NOTES.md`

Для portfolio/domain model задач дополнительно читать:

- `docs/DATA_MODEL.md`
- `docs/OWNERSHIP_AND_ISOLATION.md`
- `docs/PERMISSIONS.md`
- `docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md`

Для dashboard задач дополнительно читать:

- `docs/ADMIN_WORKFLOW.md`
- `docs/OWNERSHIP_AND_ISOLATION.md`
- `docs/PERMISSIONS.md`
- `docs/UI_DESIGN.md`

Для theme/public UI задач дополнительно читать:

- `docs/THEME_SYSTEM.md`
- `docs/PUBLIC_SITE.md`
- `docs/UI_DESIGN.md`
- `docs/MEDIA_PRESENTATION.md`

Для media/upload/viewer задач дополнительно читать:

- `docs/MEDIA_PRESENTATION.md`
- `docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md`
- `docs/SECURITY_NOTES.md`
- `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md`

Для deployment/runtime задач дополнительно читать:

- `docs/DEPLOYMENT.md`
- `docs/SECURITY_NOTES.md`
- `docs/PRIVACY_AND_OPERATOR_RESPONSIBILITIES.md`
- `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md`

Для licensing/third-party/release задач дополнительно читать:

- `docs/OPEN_SOURCE_AND_THIRD_PARTY_POLICY.md`
- `THIRD_PARTY_NOTICES.md`
- `LICENSE`
- `licenses/README.md`

Для documentation-only задач дополнительно читать:

- `docs/README.md`
- relevant topic docs
- `docs/FILE_INDEX.md`
- `docs/WORK_LOG.md`
- `docs/CHANGELOG.md`

## Обновление документации после изменений

- После осмысленных изменений обновлять `docs/PROJECT_STATE.md`.
- После осмысленных изменений добавлять запись в `docs/WORK_LOG.md`.
- Когда файлы добавлены, удалены, перемещены или переименованы, обновлять `docs/FILE_INDEX.md`.
- Когда меняется принятое архитектурное решение, обновлять `docs/DECISIONS.md` и затронутые topic docs.
- Когда меняется архитектура, обновлять `docs/ARCHITECTURE.md`.
- Когда меняется направление продукта, обновлять `docs/PRODUCT_VISION.md`.
- Когда меняются product principles, обновлять `docs/PRODUCT_PRINCIPLES.md` и `docs/DECISIONS.md`, если затронуто принятое решение.
- Когда меняются требования, обновлять `docs/REQUIREMENTS.md`.
- Когда меняются регистрация, аккаунты, email verification или onboarding, обновлять `docs/REGISTRATION_AND_ACCOUNTS.md`.
- Когда меняются ownership isolation или server-side scoping, обновлять `docs/OWNERSHIP_AND_ISOLATION.md`.
- Когда меняется account deletion или data lifecycle, обновлять `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md` и будущие тестовые требования.
- Когда меняются права доступа, роли, модерация или публикация, обновлять `docs/PERMISSIONS.md`.
- Когда меняется UX публичного сайта, обновлять `docs/PUBLIC_SITE.md` и `docs/UI_DESIGN.md`.
- Когда меняется workflow Site Administrator или Portfolio Owner, обновлять `docs/ADMIN_WORKFLOW.md`.
- Когда меняется theme system, theme registry или responsive contract, обновлять `docs/THEME_SYSTEM.md` и `docs/UI_DESIGN.md`.
- Когда меняются viewer/lightbox, captions, EXIF или media policy, обновлять `docs/MEDIA_PRESENTATION.md`.
- Когда меняется media access, public full-size delivery, copyright notice или user-content rights, обновлять `docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md`.
- Когда меняются стек или решения по зависимостям, обновлять `docs/TECH_STACK.md`.
- Когда меняются предположения по деплою, обновлять `docs/DEPLOYMENT.md`.
- Когда меняются предположения по безопасности, обновлять `docs/SECURITY_NOTES.md`.
- Когда меняется лицензия проекта, обновлять `LICENSE`, `README.md`, `docs/OPEN_SOURCE_AND_THIRD_PARTY_POLICY.md`, `THIRD_PARTY_NOTICES.md` при необходимости и `docs/FILE_INDEX.md`.
- Когда добавляются, удаляются, vendored, adapted или upgraded dependencies/assets, обновлять `THIRD_PARTY_NOTICES.md` where relevant.

## Ограничения на действия

- Не делать коммиты, если пользователь явно об этом не попросил.
- В конце осмысленного шага предлагать короткий commit message на английском.
- Не добавлять React, Next.js, микросервисы, Celery, Redis, S3 и кастомную auth-систему без отдельного явного решения.
- Не реализовывать собственное password hashing, sessions, ORM, низкоуровневую auth-логику или custom token cryptography.
- Предпочитать Django/Wagtail и зрелые библиотеки для users, sessions, permissions, registration, email verification, password reset, admin, migrations и image handling.
- Self-registered users никогда не получают `is_staff`, `is_superuser`, Wagtail Admin access, глобальные Wagtail collections или page tree permissions автоматически.
- Client-side ownership checks никогда не являются границей безопасности.
- Arbitrary user-supplied theme code, arbitrary template execution, arbitrary JavaScript injection и arbitrary CSS injection не входят в MVP.
- Raw EXIF нельзя рендерить публично; использовать только allowlist и явные настройки видимости.
- Social features нельзя вводить без отдельного явного product decision.
- Первые постоянные миграции нельзя создавать до custom User model, PostgreSQL/dev settings и initial image strategy review.
- Перед изменением standard Wagtail Image strategy нужен explicit architecture review.
- Нельзя добавлять unlicensed copied assets.
- Нельзя добавлять arbitrary commercial-use restrictions к AGPL project license.
- Нельзя изменять canonical `LICENSE` text вручную и нельзя добавлять в него third-party notices.
- User-content rights должны оставаться отдельными от software licensing.
- Fake DRM/copy-protection work запрещен без явного изменения product direction.
- Mandatory telemetry, analytics, phone-home behavior, required external CDNs/fonts или hidden tracking запрещены без явного product decision.
- Нельзя утверждать legal compliance без доказательной базы и выбранной operational policy.
- Публичный frontend держать кастомным и визуально не связанным с дефолтным видом CMS/admin.
