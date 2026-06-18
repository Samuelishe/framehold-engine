# MEDIA_PRESENTATION

## Статус

Документ описывает planned media presentation contract. Viewer/lightbox, renditions и EXIF UI пока не реализованы.

## Общие принципы

Framehold Engine должен использовать common viewer/lightbox behavior across themes. Themes могут стилизовать viewer, но core interaction и accessibility behavior должны оставаться consistent.

Framehold Engine is not an anti-copy or DRM-oriented product. Published photographs are expected to be viewable and saveable.

## Media asset concepts

### Source original

Private uploaded source file, not served directly by ordinary public media root. Может содержать full EXIF, GPS, editing metadata, original filename concerns и private metadata.

### Public full-resolution asset

Highest-quality version intentionally made available to Public Visitors. It may be generated from the source original, may be metadata-sanitized, and may differ from the raw upload. Exact implementation remains open.

### Public rendition

Resized/cropped formats for grids, feeds, cards and viewer.

Conceptual local filesystem direction:

- `private_media/sources/`
- `public_media/full/`
- `public_media/renditions/`

Do not implement these folders until media architecture is reviewed.

## Original access

Published photograph may expose Open original or Download original. Direct URL to a published full-size image is acceptable. Exact original-download controls may later be configurable at Portfolio or Photo level.

Do not use fake copy protection, browser context-menu disabling, transparent overlays, canvas-only rendering to hide sources, deliberate URL hiding or DRM.

## Title, caption, alt text, dates, EXIF

- `title` — короткое display name.
- `caption` — optional author's textual note.
- `alt_text` — accessibility description.
- `captured_at` — дата съемки.
- `uploaded_at` — timestamp загрузки.
- `EXIF` — structured technical metadata.

Caption — это не visitor comment и не social interaction.

## EXIF visibility

EXIF visibility должен быть opt-in или явно configurable.

Публичный EXIF использует allowlist, например:

- camera;
- lens;
- focal length;
- aperture;
- shutter speed;
- ISO;
- capture date.

GPS coordinates не отображаются по умолчанию. Raw EXIF JSON нельзя рендерить напрямую.

Hiding EXIF in UI does not remove embedded metadata from downloadable files. If raw uploaded source is public, embedded GPS and EXIF may also become downloadable. Raw source-original exposure, if ever allowed, must be an explicit dangerous option with a warning. Final source-original/public-original policy must address metadata sanitization.

## Presentation defaults and overrides

Portfolio defaults:

- show captions;
- show capture date;
- show EXIF.

Per-photo override:

- inherit;
- show;
- hide.

Advanced EXIF exploration остается later feature, но basic controlled metadata presentation входит в planned product.

## Desktop viewer behavior

- Click по фотографии открывает viewer.
- Escape закрывает viewer.
- Click по backdrop закрывает viewer.
- Click по самой фотографии не закрывает viewer.
- Left/Right arrow keys выполняют навигацию.
- Visible previous/next controls доступны.
- Fullscreen action доступен where supported.
- Adjacent images may be prefetched.
- Closing возвращает пользователя к previous scroll position.
- Keyboard focus возвращается к originating thumbnail.
- Page scrolling controlled while viewer is open.

## Mobile viewer behavior

- Viewer использует почти все доступное screen space.
- Swipe left/right выполняет навигацию.
- Visible close action существует.
- Browser/system back должен behave sensibly.
- Captions и EXIF не должны постоянно перекрывать большую часть изображения.
- Information button может открывать bottom sheet или expandable metadata panel.
- Fullscreen используется только where supported.

## Accessibility considerations

- Keyboard navigation.
- Visible focus.
- Meaningful controls.
- Alt text.
- Focus trapping while modal is open.
- Focus restoration after closing.
- Reduced-motion compatibility where relevant.

## Upload and rendition safety

- Uploads доступны только verified authenticated Portfolio Owners.
- Anonymous uploads запрещены.
- Permitted image formats должны быть явно определены.
- Extension alone must not be trusted.
- Image content must be decoded/validated established libraries.
- Maximum file size должен существовать.
- Maximum pixel dimensions или decompression limits должны существовать.
- Per-account или per-portfolio storage quota должен существовать.
- Upload rate limits may be required.
- Failed/partial uploads не должны создавать broken public entries.
- Original files не используются как ordinary grid thumbnails.
- Responsive renditions/previews должны генерироваться.
- Public access to originals — отдельная deliberate policy.
- Hidden/draft media не считаются private только потому, что на них нет ссылок.
- Media URL и storage access policy требуют отдельного review.
- GPS metadata не должна утекать случайно.
- Draft, hidden, suspended and deleted media must not be publicly accessible through direct media URLs controlled by Framehold Engine.
- Public `/media/` must not accidentally expose every uploaded source file.

Exact values и implementation mechanisms остаются открытыми.

## Prototype requirement before real uploads

Before implementing real uploads, create a small technical prototype or architecture spike to verify how standard Wagtail Image, renditions, local filesystem storage, and private-source/public-delivery separation can coexist.
