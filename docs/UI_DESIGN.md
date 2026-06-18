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

## Что важно не делать

- Не переносить визуальный стиль Wagtail Admin в публичную часть.
- Не превращать публичный сайт в social feed.
- Не полагаться на theme для authorization, ownership или publication policy.
- Не пытаться делать final polish до рабочего MVP.

## Приоритет

Сначала architecture for themes, safe public contexts, responsive layouts and viewer contract. Визуальная полировка идет отдельным поздним этапом.
