# REQUIREMENTS

## Функциональные требования

- Поддерживать public self-registration.
- Требовать mandatory email verification до portfolio onboarding, uploads и publication.
- Использовать email-only login as preferred initial direction.
- Поддерживать one verified user account owns one Portfolio в MVP.
- Поддерживать много независимых публичных portfolios в одной установке.
- Предоставить Framehold Dashboard для Portfolio Owners.
- Поддерживать создание, редактирование и публикацию Portfolio, Album и Photo.
- Поддерживать AlbumPhoto relation для сортировки фотографий внутри альбома.
- Поддерживать curated theme selection и safe theme settings.
- Поддерживать public viewer/lightbox across themes.
- Поддерживать controlled captions, capture dates, alt text и allowlisted EXIF.
- Поддерживать account/portfolio suspension Site Administrator.
- Поддерживать first-publication approval by Site Administrator by default.
- Поддерживать public-but-unlisted Portfolio discoverability.
- Поддерживать self-service Delete account and all data.
- Поддерживать public published-image saveability without fake DRM.
- Поддерживать separation между source original, public full-resolution asset и public rendition.
- Поддерживать third-party attribution and license inventory.

## Нефункциональные требования

- Права доступа и ownership isolation должны проверяться server-side.
- Owner-facing querysets должны быть scoped to authenticated owner's Portfolio.
- Публичная выдача должна включать только published и non-suspended content.
- Публичный интерфейс должен быть быстрым, responsive и ориентированным на изображения.
- Security должен быть proportional для MVP без enterprise-heavy требований.
- Реализация не должна полагаться на реальные приватные данные в репозитории.
- Repository governance must preserve canonical AGPL license and third-party notices.

## Public Visitor requirements

- Видеть published portfolios, albums и photographs.
- Открывать photographs в public viewer/lightbox.
- Читать author captions и enabled metadata.
- Не видеть drafts, hidden, suspended или unpublished content.
- Не загружать файлы.
- Не иметь доступа к private dashboard routes и Wagtail Admin.
- Не иметь social interaction mechanics в MVP.
- Иметь возможность сохранить или открыть published photographs according to public media policy.

## Site Administrator requirements

- Управлять всеми пользователями.
- Inspect/manage all portfolios.
- Suspend/reactivate accounts.
- Suspend/hide portfolios.
- Управлять global site settings.
- Управлять available themes.
- Управлять global CMS content.
- Access Wagtail Admin.
- Выполнять emergency corrective actions.
- View/edit any portfolio data when required.

## Portfolio Owner requirements

- Access private Framehold Dashboard.
- Edit only own Portfolio.
- Choose one available curated theme.
- Configure presentation settings allowed by that theme.
- Upload/delete own photographs.
- Create/edit own albums.
- Change photo order.
- Edit titles, captions, alt text, dates и permitted metadata.
- Publish/unpublish own content subject to final publication policy.
- Initiate Delete account and all data through Framehold Dashboard.
- Не получать Wagtail staff/admin access автоматически.

## Registration and account requirements

- Email required.
- Email unique case-insensitively.
- Email normalized consistently.
- Email is technical login identifier in accepted initial direction.
- Public identity uses `Portfolio.slug` and `Portfolio.public_name`.
- Verification links expire and are single-use.
- Resend verification has cooldown.
- Signup, login, verification resend and password reset are rate-limited.
- Administrator can disable new registrations globally.
- Password reset uses verified email channel.
- Exact auth package, rate limits and expiration values remain open.

## State requirements

- User account state is separate from Portfolio publication and moderation state.
- Portfolio publication state is separate from discoverability.
- `unlisted` means accessible by direct public URL but omitted from public catalog/index pages.
- Search indexing preference is advisory and should affect robots/meta/sitemap behavior later.
- Deletion is not suspension.
- Approval is not publication.
- Publication is not discoverability.

## First-publication moderation requirements

- Verified Portfolio Owner may create and configure Portfolio.
- Owner may upload and organize content privately.
- First public publication requires Site Administrator approval by default.
- After approval, owner may publish/unpublish/update own content unless suspended or stricter policy is enabled.
- Operator should be able to configure the policy.

## Media and upload requirements

- Uploads only for verified authenticated Portfolio Owners.
- Anonymous uploads forbidden.
- Permitted image formats explicitly defined.
- Extension alone must not be trusted.
- Images decoded/validated by established libraries.
- Maximum file size and pixel/decompression limits required.
- Per-account or per-portfolio storage quota required.
- Responsive renditions/previews generated.
- Public access to originals is a deliberate policy decision.
- Private source originals and public delivery assets are separate concepts.
- GPS metadata must not leak accidentally.
- Draft, hidden, suspended and deleted media must not become public merely because a URL is known.
- A public `/media/` directory must not accidentally expose every uploaded source file.
- Public original/download controls may be configurable later.

## Account deletion requirements

- User-facing action: Delete account and all data.
- Require re-authentication or sufficiently recent authenticated session.
- Require explicit irreversible confirmation.
- Remove public access immediately.
- Revoke sessions and block login/edit/upload operations.
- Delete owned active application data and controlled media assets.
- Deletion must be idempotent and retryable.
- Deletion must not affect other users' accounts, portfolios or media.
- Sole Site Administrator protection is required.

## Content rights and attribution requirements

- User content is not automatically AGPL-licensed.
- Portfolio Owners must upload only content they have rights to use.
- Downloading a public photograph does not grant reuse permission.
- Future public UI should display concise copyright/content-rights notice.
- Third-party code/assets require provenance and license review.
- `THIRD_PARTY_NOTICES.md` must be updated when relevant material is included or adapted.

## Operator/legal-page requirements

- Future configurable pages should cover Privacy Policy, Terms of Service, license information, third-party notices, contact and copyright/content complaints.
- Framehold Engine must not claim automatic legal compliance for every deployment.

## Theme requirements

- Themes are trusted code-defined presets shipped with Framehold Engine.
- Portfolio Owner may select installed themes but may not upload theme code.
- Theme settings are stored as validated safe configuration.
- Theme settings include versioning through `theme_settings_version`.
- Themes must provide desktop, tablet and mobile behavior.
- Missing theme falls back to a safe default theme.

## MVP requirements

- Custom User model before first application migrations.
- Registration, email verification, login/logout and password reset.
- Portfolio onboarding.
- Portfolio, Album, Photo, AlbumPhoto and SiteSettings domain.
- Ownership isolation and permission tests.
- Framehold Dashboard.
- Minimal Justified public theme.
- Renditions and common viewer/lightbox.

## Out of scope for early versions

- Visitor comments, likes, follows, activity feeds, DMs, ratings.
- Anonymous public uploads.
- User-uploaded theme packages.
- Private/password-protected albums.
- Tags and full search.
- Advanced EXIF exploration.
- Collaborators.
- S3/R2 as initial storage.
- Data export before deletion.
