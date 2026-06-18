# AGENTS.md

## Язык и стиль

- Отвечать пользователю на русском языке.
- Комментарии и docstring в коде писать на русском языке там, где это действительно полезно.
- Корневой `README.md` должен оставаться на английском языке как GitHub landing page.
- Внутренние документы в `docs/` и отчеты Codex пользователю писать на русском языке. Technical identifiers and established technology names may remain in English.

## Что читать перед началом работы

Перед началом любой осмысленной работы прочитать:

- `docs/README.md`
- `docs/PROJECT_STATE.md`
- `docs/PRODUCT_VISION.md`
- `docs/ROADMAP.md`
- `docs/WORK_LOG.md`
- `docs/ARCHITECTURE.md`
- `docs/REQUIREMENTS.md`
- `docs/DATA_MODEL.md`
- `docs/PERMISSIONS.md`
- `docs/REGISTRATION_AND_ACCOUNTS.md`
- `docs/OWNERSHIP_AND_ISOLATION.md`
- `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md`
- `docs/PUBLIC_SITE.md`
- `docs/ADMIN_WORKFLOW.md`
- `docs/THEME_SYSTEM.md`
- `docs/MEDIA_PRESENTATION.md`
- `docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md`
- `docs/OPEN_SOURCE_AND_THIRD_PARTY_POLICY.md`
- `docs/PRIVACY_AND_OPERATOR_RESPONSIBILITIES.md`
- `docs/UI_DESIGN.md`
- `docs/TECH_STACK.md`
- `docs/DEVELOPMENT.md`
- `docs/DEPLOYMENT.md`
- `docs/SECURITY_NOTES.md`
- `docs/CODING_RULES.md`
- `docs/FILE_INDEX.md`

## Обновление документации после изменений

- После осмысленных изменений обновлять `docs/PROJECT_STATE.md`.
- После осмысленных изменений добавлять запись в `docs/WORK_LOG.md`.
- Когда файлы добавлены, удалены, перемещены или переименованы, обновлять `docs/FILE_INDEX.md`.
- Когда меняется архитектура, обновлять `docs/ARCHITECTURE.md`.
- Когда меняется направление продукта, обновлять `docs/PRODUCT_VISION.md`.
- Когда меняются требования, обновлять `docs/REQUIREMENTS.md`.
- Когда меняются регистрация, аккаунты, email verification или onboarding, обновлять `docs/REGISTRATION_AND_ACCOUNTS.md`.
- Когда меняются ownership isolation или server-side scoping, обновлять `docs/OWNERSHIP_AND_ISOLATION.md`.
- Когда меняется account deletion или data lifecycle, обновлять `docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md` и будущие тестовые требования.
- Когда меняются правила прав доступа, авторства или публикации, обновлять `docs/PERMISSIONS.md`.
- Когда меняется UX публичного сайта, обновлять `docs/PUBLIC_SITE.md` и `docs/UI_DESIGN.md`.
- Когда меняется workflow Site Administrator или Portfolio Owner, обновлять `docs/ADMIN_WORKFLOW.md`.
- Когда меняется theme system, theme registry или responsive contract, обновлять `docs/THEME_SYSTEM.md` и `docs/UI_DESIGN.md`.
- Когда меняются viewer/lightbox, captions, EXIF или media policy, обновлять `docs/MEDIA_PRESENTATION.md`.
- Когда меняется media access, public originals, copyright notice или user-content rights, обновлять `docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md`.
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
- Предпочитать встроенные механизмы Django/Wagtail и зрелые библиотеки для пользователей, сессий, прав, регистрации, email verification, password reset, админки, миграций и изображений.
- Никогда не выдавать self-registered users `is_staff`, `is_superuser`, Wagtail admin access, глобальные Wagtail collections или page tree permissions автоматически.
- Никогда не считать client-side ownership checks границей безопасности.
- Никогда не добавлять произвольный пользовательский theme code, arbitrary template execution, arbitrary JavaScript injection или arbitrary CSS injection в MVP.
- Никогда не рендерить raw EXIF публично; использовать только allowlist и явные настройки видимости.
- Никогда не вводить social features без отдельного явного product decision.
- Никогда не создавать первые постоянные миграции до review custom User model и standard Wagtail Image strategy.
- Portfolio и Album являются regular Django models в принятой архитектуре, не Wagtail Pages.
- Photo является Framehold domain model и initially references the standard Wagtail Image model.
- Перед изменением standard Wagtail Image strategy нужен explicit architecture review.
- Никогда не выдавать self-registered users Wagtail staff access автоматически.
- Никогда не добавлять unlicensed copied assets.
- Никогда не добавлять arbitrary commercial-use restrictions к AGPL project license.
- Никогда не изменять canonical `LICENSE` text вручную и не добавлять в него third-party notices.
- User-content rights должны оставаться отдельными от software licensing.
- Никогда не делать fake DRM/copy-protection work без явного изменения product direction.
- Никогда не утверждать legal compliance без доказательной базы и выбранной operational policy.
- Публичный frontend держать кастомным и визуально не связанным с дефолтным видом CMS/admin.
