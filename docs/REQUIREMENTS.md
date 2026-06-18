# REQUIREMENTS

## Функциональные требования

- Поддерживать public self-registration.
- Требовать mandatory email verification до portfolio onboarding, uploads и publication.
- Поддерживать one verified user account owns one Portfolio в MVP.
- Поддерживать много независимых публичных portfolios в одной установке.
- Предоставить Framehold Dashboard для Portfolio Owners.
- Поддерживать создание, редактирование и публикацию Portfolio, Album и Photo.
- Поддерживать AlbumPhoto relation для сортировки фотографий внутри альбома.
- Поддерживать curated theme selection и safe theme settings.
- Поддерживать public viewer/lightbox across themes.
- Поддерживать controlled captions, capture dates, alt text и allowlisted EXIF.
- Поддерживать account/portfolio suspension Site Administrator.

## Нефункциональные требования

- Права доступа и ownership isolation должны проверяться server-side.
- Owner-facing querysets должны быть scoped to authenticated owner's Portfolio.
- Публичная выдача должна включать только published и non-suspended content.
- Публичный интерфейс должен быть быстрым, responsive и ориентированным на изображения.
- Security должен быть proportional для MVP без enterprise-heavy требований.
- Реализация не должна полагаться на реальные приватные данные в репозитории.

## Public Visitor requirements

- Видеть published portfolios, albums и photographs.
- Открывать photographs в public viewer/lightbox.
- Читать author captions и enabled metadata.
- Не видеть drafts, hidden, suspended или unpublished content.
- Не загружать файлы.
- Не иметь доступа к private dashboard routes и Wagtail Admin.
- Не иметь social interaction mechanics в MVP.

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
- Не получать Wagtail staff/admin access автоматически.

## Registration and account requirements

- Email required.
- Email unique case-insensitively.
- Email normalized consistently.
- Verification links expire and are single-use.
- Resend verification has cooldown.
- Signup, login, verification resend and password reset are rate-limited.
- Administrator can disable new registrations globally.
- Password reset uses verified email channel.
- Exact auth package, rate limits and expiration values remain open.

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
- GPS metadata must not leak accidentally.

## Theme requirements

- Themes are trusted code-defined presets shipped with Framehold Engine.
- Portfolio Owner may select installed themes but may not upload theme code.
- Theme settings are stored as validated safe configuration.
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
