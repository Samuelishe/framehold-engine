# MEDIA_PRESENTATION

## Статус

Документ описывает planned media presentation contract. Viewer/lightbox, renditions и EXIF UI пока не реализованы.

## Общие принципы

Framehold Engine должен использовать common viewer/lightbox behavior across themes. Themes могут стилизовать viewer, но core interaction и accessibility behavior должны оставаться consistent.

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

Exact values и implementation mechanisms остаются открытыми.
