# CODING_RULES

## Общие правила

- Использовать type hints там, где это улучшает читаемость.
- Держать Django apps сфокусированными.
- Не переносить доменные правила в templates.
- Authorization всегда server-side.
- Не использовать broad `except` без причины.
- Не проглатывать exceptions silently.
- Не хардкодить secrets.
- Не конкатенировать filesystem paths вручную там, где лучше `pathlib`.
- Do not rely on case-insensitive filesystem behavior.
- Deployment/runtime docs and examples should use POSIX-style paths.
- Держать migrations reviewable.
- Избегать overengineering.
- Не добавлять dependencies без понятной причины.

## Auth and accounts

- Custom User must exist before first permanent application migrations.
- Use established libraries/mechanisms for registration, email verification and password reset.
- Do not implement custom password hashing.
- Do not implement custom session handling.
- Do not implement custom token cryptography.
- Self-registered users are not staff by default.
- Email-only login is the preferred initial direction.

## Ownership and query rules

- Owner-facing queries must always be scoped to authenticated owner's Portfolio.
- Templates must not perform unrestricted domain queries.
- Public rendering receives already filtered safe context.
- Direct object access checks must be server-side.
- Forged IDs in POST data must not cross ownership boundaries.
- No broad deletion querysets.
- Destructive operations must be explicitly scoped.
- User-supplied object IDs require ownership validation.
- Some invariants require server-side validation and tests, not only database constraints.

## Themes

- No arbitrary theme execution.
- No user-uploaded theme code in MVP.
- Theme settings must be validated by schema.
- Theme settings need versioning through `theme_settings_version`.
- Unknown theme settings must not be executed.
- Changing a theme must not mutate Album or Photo data.
- Themes must not control authorization, ownership, authentication, publication policy or access to drafts.

## Media and EXIF

- Public EXIF uses an allowlist.
- Raw EXIF JSON is never rendered publicly.
- GPS is hidden by default.
- Uploaded image content must be validated by established image libraries.
- Originals must not be casually exposed without explicit policy.
- Private source originals and public delivery assets are separate concepts.
- Media authorization must be server-side.
- Do not use fake DRM.

## Account deletion

- Future account deletion code must be idempotent and testable.
- Filesystem/object-storage cleanup cannot rely only on database cascades.
- Partial cleanup must be retryable.
- Owner A deletion must never affect Owner B.
- Public routes and public media URLs controlled by Framehold Engine must stop serving deleted assets.

## Licensing and third-party material

- Preserve SPDX/license headers where introduced.
- Do not add third-party code or assets without recorded provenance.
- Do not edit canonical root `LICENSE`.
- Do not place third-party notices into `LICENSE`; use `THIRD_PARTY_NOTICES.md`.
- Do not add unverified copied assets, proprietary fonts, unlicensed screenshots or stock media without redistribution rights.

## Django/Wagtail

Use Django/Wagtail built-ins for auth, sessions, permissions, admin, migrations and image handling where appropriate, but keep Portfolio Owner UI in Framehold Dashboard, not ordinary Wagtail Admin.
