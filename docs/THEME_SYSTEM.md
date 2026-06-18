# THEME_SYSTEM

## Статус

Curated theme system — определяющая capability Framehold Engine, а не distant future idea. Реализации пока нет.

## Определение

Theme — доверенный code-defined presentation preset, поставляемый вместе с Framehold Engine. Portfolio Owner может выбрать installed theme и настроить безопасные параметры, но не может загружать или редактировать произвольный HTML, CSS, JavaScript, Python или template code.

Built-in themes must serve assets locally or use system font stacks. They must not require Google Fonts, public CDN JavaScript, analytics, trackers, telemetry or project phone-home behavior.

## Conceptual ThemeDefinition

- `key`
- `display_name`
- `version`
- `preview_image`
- `portfolio_template`
- `album_template`
- `stylesheet/assets`
- `settings_schema`
- `supported_capabilities`
- `mobile_behavior`
- `fallback_behavior`

В базе хранятся только безопасные настройки:

- `theme_key`
- validated `theme_settings`
- `theme_settings_version`

Theme code остается в repository/application.

## Что theme может контролировать

- typography;
- colors;
- background;
- navigation position;
- gallery layout;
- spacing;
- caption placement;
- metadata placement;
- lightbox styling;
- desktop/tablet/mobile presentation.

## Что theme не может контролировать

- authorization;
- ownership;
- authentication;
- publication policy;
- access to drafts;
- access to another user's data;
- whether sensitive EXIF/GPS is permitted;
- unrestricted database queries.
- media authorization;
- required copyright/license notices controlled by the application.
- telemetry, analytics or external service activation.

Themes получают prepared and safely filtered public context.

## Запреты MVP

- User-uploaded theme packages.
- Arbitrary template execution.
- Arbitrary JavaScript injection.
- Arbitrary CSS injection.
- Per-photo layout fields tightly coupled to one specific theme.
- Fake copy protection such as context-menu blocking, transparent overlays or canvas-only rendering to hide image URLs.

Theme-specific settings должны валидироваться schema выбранной темы. Если выбранная тема больше не существует, Framehold Engine должен перейти на safe default theme.

Themes may style Open full size / Download full size controls, but must not override media authorization or hide required application-level licensing/copyright notices.

Built-in safe default theme: `minimal_justified`. It is always shipped, works with empty/default settings, is used for onboarding, and is fallback when stored `theme_key` is missing/invalid or settings cannot be migrated safely.

## Theme settings versioning

- User stores only safe validated settings.
- Unknown settings must not be executed.
- Changing a theme must not mutate Album or Photo data.
- Theme updates may require settings migration.
- System should eventually support migrating settings between theme versions.
- Preview before applying a theme is desirable.
- Per-photo grid coordinates tied to one theme must not be stored in the core domain model.

## Safe rendering contract

Themes receive prepared rendering structures, such as implementation-neutral equivalents of `PublicPortfolioViewModel`, `PublicAlbumViewModel`, and `PublicPhotoViewModel`.

Prepared context may contain public Portfolio identity, safe navigation, ordered public Portfolio Photos, ordered public Albums, ordered public Album Photos, resolved caption/date/EXIF visibility, resolved public rendition URLs, resolved public full-size URL where allowed, common viewer configuration, and copyright/content-rights notice.

Themes must not receive unrestricted global Photo/Album QuerySets, ownership-sensitive model collections, unpublished objects, raw EXIF JSON, private source paths, or authentication/permission controls.

Themes present data; application/domain layers decide which data is safe to present.

Themes may style Open full size / Download full size controls, but must not imply raw source original exposure.

## Responsive contract

Desktop:

- theme-specific sidebar, header, grid, justified layout или mosaic.

Tablet:

- reduced column count;
- compact navigation;
- preserved image readability.

Mobile:

- top navigation или compact menu;
- обычно single-column vertical photo feed;
- full-width images where practical;
- captions near photographs in the feed;
- no permanent metadata panel stealing useful image area;
- touch-friendly controls.

Mobile fallback должен оставаться предсказуемым, даже если desktop theme использует complex mosaic. Desktop и mobile не должны становиться двумя несвязанными продуктами.

## Initial theme families

### Minimal Justified

Первый рекомендуемый reference theme: light editorial presentation, optional desktop sidebar, justified rows, mixed image aspect ratios, little or no destructive crop, single-column mobile feed.

### Classic Grid

Regular card/grid layout, consistent rhythm, possible cropping and focal points, one or two columns on small screens.

### Nocturne Mosaic

Dark presentation, asymmetric editorial mosaic, более сложный layout. Планируется после более простых тем; mobile fallback становится стабильным vertical feed.

### Journal Feed

Large photographs in a vertical editorial sequence, captions and dates near the photograph, особенно подходит для mobile.

## Приоритет

Финальная визуальная полировка остается более поздним этапом, но theme architecture должна существовать до реализации нескольких публичных layouts.

Operator-installed third-party themes may be future work. Arbitrary Portfolio Owner uploaded themes are not an MVP feature and should be treated as high-risk/non-goal unless explicitly reapproved.
