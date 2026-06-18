# THEME_SYSTEM

## Статус

Curated theme system — определяющая capability Framehold Engine, а не distant future idea. Реализации пока нет.

## Определение

Theme — доверенный code-defined presentation preset, поставляемый вместе с Framehold Engine. Portfolio Owner может выбрать installed theme и настроить безопасные параметры, но не может загружать или редактировать произвольный HTML, CSS, JavaScript, Python или template code.

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

Themes получают prepared and safely filtered public context.

## Запреты MVP

- User-uploaded theme packages.
- Arbitrary template execution.
- Arbitrary JavaScript injection.
- Arbitrary CSS injection.
- Per-photo layout fields tightly coupled to one specific theme.
- Fake copy protection such as context-menu blocking, transparent overlays or canvas-only rendering to hide image URLs.

Theme-specific settings должны валидироваться schema выбранной темы. Если выбранная тема больше не существует, Framehold Engine должен перейти на safe default theme.

Themes may style Open original / Download original controls, but must not override media authorization or hide required application-level licensing/copyright notices.

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
