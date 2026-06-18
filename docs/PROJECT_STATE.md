# PROJECT_STATE

## Текущее состояние

- Проект остается на стадии документационного фундамента и product refinement.
- Django-проект еще не инициализирован.
- Wagtail еще не инициализирован.
- Прикладного кода нет.
- Миграций, моделей, views, templates, CSS, JavaScript, форм, тестов, email integration и Docker configuration нет.
- Production deployment еще не существует.
- Корневой `README.md` теперь является GitHub landing page на английском языке.

## Принятые продуктовые уточнения

- Framehold Engine теперь определяется как self-hosted multi-user, multi-portfolio web gallery engine.
- Public registration с mandatory email verification является core capability.
- Framehold Dashboard является core product component для Portfolio Owners, а не optional future fallback.
- Curated theme system является defining capability, а не distant future idea.
- Multi-portfolio ownership isolation является hard requirement.
- Лицензия проекта: GNU Affero General Public License version 3 or later, SPDX `AGPL-3.0-or-later`.
- Portfolio и Album приняты как regular Django domain models, не Wagtail Pages.
- Photo принят как Framehold domain model, который initially references the standard Wagtail Image model.
- Custom Wagtail image model не планируется для initial implementation.
- Preferred initial login direction: email-only login; public identity belongs to Portfolio through `slug` and `public_name`.
- One domain `Photo` corresponds to one standard Wagtail Image asset in the MVP; reuse across albums happens through `AlbumPhoto`.
- Private source originals, public full-resolution assets and public renditions are separate architectural concepts.
- Production hosting assumption: Linux VPS, typically Ubuntu or another Debian-like server.
- Repository hygiene now includes `.editorconfig` and `.gitattributes` for stable formatting and LF normalization.
- Account deletion and all data является core product requirement.
- Published photographs are expected to be viewable and saveable; Framehold Engine не является DRM/anti-copy продуктом.
- Исходный сценарий Irwyn, Polina и отца Irwyn остается первым intended use case, но не ограничивает продукт.

## Что уже сделано

- Создан корневой README.
- Создан `AGENTS.md` с правилами для будущих агентских сессий.
- Создан базовый комплект документов в `docs/`.
- Добавлен и уточнен `.gitignore` для Python/Django/Wagtail-репозитория, включая исключение локальных артефактов PyCharm.
- Обновлена документация под модель public registration, Portfolio Owner, Framehold Dashboard, curated themes и media presentation.
- Добавлены документы по account deletion/data lifecycle, content rights/media access, open-source/third-party policy и privacy/operator responsibilities.
- Добавлены root `LICENSE`, `THIRD_PARTY_NOTICES.md` и `licenses/README.md`.

## Следующие архитектурные вопросы

Перед инициализацией доменной реализации нужно явно решить:

- exact authentication package для registration, verification и password reset;
- canonical public URL scheme: `/photographers/<slug>/`, `/portfolio/<slug>/` или другой стабильный route.
- exact quotas and upload limits;
- exact private-source/public-delivery media storage implementation;
- exact storage cleanup strategy for source originals, public full-resolution assets and renditions.

## Следующий шаг

Следующий осмысленный архитектурный шаг — technical spike for standard Wagtail Image, renditions and private-source/public-delivery separation before real upload implementation.
