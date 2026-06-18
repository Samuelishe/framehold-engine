# UI_DESIGN

## Общее направление

Публичный интерфейс должен ощущаться как premium photo portfolio или photo journal, а не как стандартная админка, social network или шаблонный Bootstrap-сайт.

## Ключевые принципы

- Минимальная навигация.
- Сильная типографика.
- Приоритет фотографий над декоративным UI.
- Хорошие отступы и спокойный ритм страницы.
- Responsive design with mobile-first sanity.
- Высококачественные previews/renditions.
- Captions and metadata near photographs when enabled.
- Common viewer/lightbox across themes.
- Clear Open original / Download original controls when enabled.
- Clear visibility controls for public/listed/unlisted semantics where applicable.
- No visitor comments, likes, follows or activity feed.

## Theme families

### Minimal Justified

Первый reference theme: light editorial presentation, optional desktop sidebar, justified rows, mixed aspect ratios, little or no destructive crop, single-column mobile feed.

### Classic Grid

Regular grid/card rhythm, possible cropping and focal points, one or two columns on small screens.

### Nocturne Mosaic

Dark asymmetric editorial mosaic. Более сложная тема после простых layouts; mobile fallback becomes stable vertical feed.

### Journal Feed

Large vertical editorial sequence with captions and dates near photographs. Особенно подходит для mobile.

## Responsive rules

Desktop can use theme-specific sidebar, header, grid, justified layout or mosaic.

Tablet should reduce column count, keep navigation compact and preserve image readability.

Mobile should use top navigation or compact menu, usually a single-column vertical feed, full-width images where practical, captions near photographs and touch-friendly controls. Permanent metadata panels must not steal useful image area.

## Viewer behavior

Viewer must support keyboard navigation, visible previous/next controls, Escape close, backdrop close, mobile swipe, visible close action, fullscreen where supported, focus trapping and focus restoration. Themes may style the viewer but should not redefine core behavior.

## Account deletion UX

Framehold Dashboard settings must include a clear danger-zone flow for Delete account and all data:

- clear list of deleted data;
- re-authentication or recent-session confirmation;
- explicit irreversible confirmation;
- no accidental one-click deletion.

## Public-but-unlisted UX

UI should explain that unlisted means "available by direct link, hidden from public indexes" and not "private". It must not present unlisted mode as access control.

## Что важно не делать

- Не переносить визуальный стиль Wagtail Admin в публичную часть.
- Не превращать публичный сайт в social feed.
- Не полагаться на theme для authorization, ownership или publication policy.
- Не добавлять deceptive anti-copy controls.
- Не пытаться делать final polish до рабочего MVP.

## Приоритет

Сначала architecture for themes, safe public contexts, responsive layouts and viewer contract. Визуальная полировка идет отдельным поздним этапом.
