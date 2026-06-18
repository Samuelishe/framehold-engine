# CHANGELOG

## Architecture cleanup and repository hygiene

- Added `docs/DECISIONS.md` architectural decision log.
- Refactored `AGENTS.md` into baseline and task-specific reading rules.
- Clarified User/Portfolio/Album/Photo/Wagtail Image cardinalities and invariants.
- Accepted email-only login as the preferred initial direction.
- Documented public-but-unlisted Portfolio discoverability.
- Documented first-publication approval as default moderation policy.
- Refined private-source/public-delivery media architecture.
- Added theme settings versioning.
- Added Linux VPS / Ubuntu-like production assumption.
- Added `.editorconfig` and `.gitattributes`.

## Licensing and data lifecycle refinement

- Added AGPL-3.0-or-later project license.
- Rewrote root README as English GitHub landing page.
- Finalized initial model direction: custom User, Portfolio and Album as regular Django models, Framehold Photo referencing standard Wagtail Image.
- Documented self-service Delete account and all data.
- Documented public media saveability and no-DRM policy.
- Added third-party attribution and asset provenance policy.
- Documented separation between software license and user-content rights.

## Product refinement: multi-portfolio engine

- Продуктовое определение обновлено до self-hosted multi-user, multi-portfolio web gallery engine.
- Зафиксированы public registration, mandatory email verification и account onboarding.
- Framehold Dashboard стал core component для Portfolio Owners.
- Curated theme system стал defining capability.
- Добавлены требования к common media viewer/lightbox, captions, dates и controlled EXIF.
- Уточнены роли Site Administrator, Portfolio Owner и Public Visitor.

## Documentation foundation

- Создан исходный документационный каркас проекта.
- Зафиксированы цели, требования, стек, архитектурное направление и правила дальнейшей работы.
