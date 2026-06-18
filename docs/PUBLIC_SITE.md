# PUBLIC_SITE

## Статус

Публичный сайт пока не реализован. Этот документ описывает planned theme-driven public presentation.

## URL scheme

Canonical public URL scheme остается открытым решением.

Варианты:

- `/photographers/<slug>/`
- `/portfolio/<slug>/`
- другой стабильный route

Дополнительные routes могут включать:

- `/`
- `/portfolios/`
- `/portfolio/<slug>/albums/<album-slug>/`
- `/about/`
- `/contact/`

Финальный вариант нужно выбрать до реализации public routes и canonical links.

## Theme-driven portfolio pages

Публичные Portfolio pages рендерятся выбранной curated theme. Theme получает prepared and safely filtered public context и не выполняет unrestricted domain queries.

Portfolio page может включать:

- public name;
- bio;
- avatar/cover;
- selected albums;
- recent or featured photographs;
- theme-specific navigation;
- captions, dates and enabled EXIF according to settings.

## Album pages

Album page показывает только published Photo из published Album внутри published non-suspended Portfolio. Layout зависит от theme, но public viewer/lightbox behavior остается common.

## Public viewer

Viewer/lightbox должен поддерживать desktop keyboard navigation, mobile swipe, visible close, fullscreen where supported, focus trapping and restoration, captions and controlled metadata. Подробно: `docs/MEDIA_PRESENTATION.md`.

## Public filtering rules

- Only published content is public.
- Suspended accounts/portfolios are not public.
- Drafts, hidden content and unpublished media are not public.
- Public rendering receives already filtered safe context.
- Public pages must not expose raw EXIF or GPS by default.

## Non-social positioning

Публичный сайт не включает visitor comments, likes, follows, public activity feed, direct messages, ratings, anonymous uploads или mandatory social sharing buttons в MVP.
