# PUBLIC_SITE

## Статус

Публичный сайт пока не реализован. Этот документ описывает planned theme-driven public presentation.

## Canonical URL scheme

- `/` — operator-managed instance homepage.
- `/portfolios/` — directory of listed public Portfolios when enabled.
- `/portfolio/<portfolio_slug>/` — canonical public Portfolio URL.
- `/portfolio/<portfolio_slug>/albums/<album_slug>/` — canonical public Album URL.
- `/accounts/` — registration, verification, login, logout and password-reset routes.
- `/dashboard/` — Framehold Dashboard.
- `/admin/` — Wagtail Admin.

Portfolio public URL never depends on User.email or authentication credentials. `Portfolio.slug` is globally unique, preferably case-insensitively. `Album.slug` is unique within its Portfolio. Canonical links must use the accepted canonical route.

`/photographers/<slug>/` is not the accepted canonical route. Separate public Photo detail page is not part of MVP. Photos open from Portfolio or Album through the common viewer. Deep links to viewer items may be considered later.

## Instance homepage and directory

Instance homepage `/` is operator-managed landing page. It may contain site introduction, registration/login actions, manually selected or featured Portfolios, and About/Contact navigation. It must not become an algorithmic social activity feed.

Portfolio directory `/portfolios/` contains only listed, publicly visible Portfolios. It may be disabled globally by the operator. It does not imply follows, popularity ranking, or social discovery mechanics.

Conceptual global setting: `directory_enabled = true`.

Default direction: directory enabled, new published Portfolio listed by default, search indexing allowed by default. Operator and Portfolio Owner may choose stricter visibility explicitly.

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

## Public-but-unlisted portfolios

A Portfolio may be public but unlisted.

Meaning:

- direct URL works;
- published content is viewable by visitors with the link;
- Portfolio is not shown in public catalog/index pages;
- this is not the same as private/password-protected albums;
- this is not a security boundary;
- it is a discoverability setting.

Conceptual settings: publication state or `is_public`, `is_listed`, `allow_search_indexing`.

Example: photographer shares a portfolio link with specific people without appearing on global `/portfolios/` or `/photographers/` index.

## Album pages

Album page показывает только published Photo из published Album внутри published non-suspended Portfolio. Layout зависит от theme, но public viewer/lightbox behavior остается common.

## Portfolio main gallery

Portfolio page can show Photos directly without requiring Album membership.

- `show_in_portfolio_gallery` controls whether published Photo appears in main Portfolio gallery.
- `portfolio_sort_order` controls main Portfolio gallery order.
- `AlbumPhoto.sort_order` controls order inside Album.
- Theme layout may change visual arrangement but must preserve resolved semantic order where accessibility/navigation requires it.
- Switching themes must not rewrite Photo or AlbumPhoto order.

## Album covers

`Album.cover_photo` is optional. It must belong to the same Portfolio as Album and be connected to that Album through AlbumPhoto. If no explicit cover is selected, use first publicly visible Photo in Album order. If Album has no public Photo, theme uses neutral placeholder. Cover fallback must not expose unpublished Photo.

## Public viewer

Viewer/lightbox должен поддерживать desktop keyboard navigation, mobile swipe, visible close, fullscreen where supported, focus trapping and restoration, captions and controlled metadata. Подробно: `docs/MEDIA_PRESENTATION.md`.

## Published photograph access

Framehold Engine не является DRM/anti-copy продуктом. Published photographs are expected to be viewable and saveable by visitors.

Запрещено использовать fake protection:

- отключение browser context menu как protection mechanism;
- transparent overlays для блокировки saving;
- canvas-only rendering для сокрытия source;
- deliberate hiding of image URLs as security mechanism;
- DRM.

A published photograph may expose Open full size or Download full size. A direct URL to a published full-size image is acceptable, subject to final media-storage policy.

## Public filtering rules

- Only published content is public.
- Suspended accounts/portfolios are not public.
- Unlisted public portfolios are public by direct URL, but omitted from indexes/catalog pages.
- Drafts, hidden content and unpublished media are not public.
- Public rendering receives already filtered safe context.
- Public pages must not expose raw EXIF or GPS by default.
- Draft, hidden, suspended or deleted media must not become public merely because a storage filename or URL is known.

## Public visibility predicates

Portfolio is publicly accessible only when User account is active, not suspended, not deletion_pending, Portfolio publication state is published, Portfolio is not administratively suspended, and current publication approval policy is satisfied if approval is enabled.

Album is publicly accessible only when parent Portfolio is publicly accessible, Album publication state is published, and Album belongs to that Portfolio.

Photo is publicly accessible in main Portfolio gallery only when parent Portfolio is publicly accessible, Photo publication state is published, Photo belongs to that Portfolio, and Photo is configured to appear in main Portfolio gallery.

Photo is publicly accessible through Album only when parent Portfolio is publicly accessible, Album is published, Photo is published, AlbumPhoto connects that Album and Photo, and Album and Photo belong to same Portfolio.

Listed/unlisted affects discovery, not direct public access. Unpublished Portfolio hides all nested Albums and Photos. Unpublished Album cannot expose Photos through Album route. Published Album cannot expose unpublished Photo. Suspension overrides ordinary publication.

## Copyright notice direction

Public UI should be able to display concise copyright/content-rights notice. Downloadable does not mean freely reusable. User photographs remain user content, not AGPL-licensed project code.

## Non-social positioning

Публичный сайт не включает visitor comments, likes, follows, public activity feed, direct messages, ratings, anonymous uploads или mandatory social sharing buttons в MVP.
