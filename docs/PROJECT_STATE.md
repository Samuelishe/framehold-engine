# PROJECT_STATE

## Текущее состояние

- Проект остается на стадии документационного фундамента и product refinement.
- Django-проект еще не инициализирован.
- Wagtail еще не инициализирован.
- Прикладного кода нет.
- Миграций, моделей, views, templates, CSS, JavaScript, форм, тестов, email integration и Docker configuration нет.
- Production deployment еще не существует.

## Принятые продуктовые уточнения

- Framehold Engine теперь определяется как self-hosted multi-user, multi-portfolio web gallery engine.
- Public registration с mandatory email verification является core capability.
- Framehold Dashboard является core product component для Portfolio Owners, а не optional future fallback.
- Curated theme system является defining capability, а не distant future idea.
- Multi-portfolio ownership isolation является hard requirement.
- Исходный сценарий Irwyn, Polina и отца Irwyn остается первым intended use case, но не ограничивает продукт.

## Что уже сделано

- Создан корневой README.
- Создан `AGENTS.md` с правилами для будущих агентских сессий.
- Создан базовый комплект документов в `docs/`.
- Добавлен и уточнен `.gitignore` для Python/Django/Wagtail-репозитория, включая исключение локальных артефактов PyCharm.
- Обновлена документация под модель public registration, Portfolio Owner, Framehold Dashboard, curated themes и media presentation.

## Следующие архитектурные вопросы

Перед инициализацией доменной реализации нужно явно решить:

- image model strategy: default Wagtail Image, custom Wagtail image model или controlled image asset model;
- Portfolio/Album representation: regular Django models, Wagtail Page models или hybrid approach;
- exact authentication package для registration, verification и password reset;
- publication approval policy: требуется ли approval Site Administrator для первой публичной публикации;
- canonical public URL scheme: `/photographers/<slug>/`, `/portfolio/<slug>/` или другой стабильный route.

## Следующий шаг

Следующий осмысленный шаг — архитектурное обсуждение image model strategy и Portfolio/Album representation до первых постоянных миграций.
