# OWNERSHIP_AND_ISOLATION

## Статус

Ownership isolation — hard requirement для multi-portfolio Framehold Engine. Это не обязательно enterprise SaaS multitenancy, но серверная изоляция портфолио обязательна.

## MVP ownership model

- One verified user account owns one Portfolio.
- One Portfolio belongs to exactly one Portfolio Owner.
- One-account-one-portfolio limitation may be relaxed later.
- Site Administrator may manage all portfolios.
- A User may be Site Administrator and also own a Portfolio.
- Site Administrator abilities must not bypass deletion-isolation expectations accidentally.

## Server-side invariants

- Every owner-facing queryset must be scoped to the authenticated owner's portfolio.
- Object visibility in the UI is not a security boundary.
- Direct access to another owner's edit/delete URL must be rejected.
- Forged form IDs must not allow selecting another owner's objects.
- Another owner's image must not be usable as an album cover.
- Another owner's Wagtail Image asset must not be selectable in owner-facing flows.
- Forged POSTed Photo ID must not allow selecting another owner's Photo as Album cover.
- `Album.cover_photo`, when set, must be connected to that Album through AlbumPhoto.
- Another owner's theme settings must not be editable.
- Another owner's unpublished content must never appear in dashboard queries.
- Public queries must return only published and non-suspended content.
- Templates must not query unrestricted global `Photo` or `Album` collections.
- Public rendering must receive an already filtered, safe context.
- Deleting Owner A must never remove Owner B's data.
- Deletion cleanup must be scoped to the deleting owner's account and Portfolio.
- Direct media URLs for deleted content controlled by Framehold Engine must stop working.
- Reusing a Photo across albums must not duplicate the underlying image asset.
- `AlbumPhoto.album.portfolio` must match `AlbumPhoto.photo.portfolio`.

## Dashboard isolation

Framehold Dashboard показывает и изменяет только текущий Portfolio текущего Portfolio Owner. Любой handler, form, queryset и service, работающий в owner-facing контексте, должен получать owner/portfolio boundary явно или выводить его из authenticated user на сервере.

## Public filtering

Публичная выдача не должна опираться на скрытие элементов в шаблоне. Querysets и public context должны быть заранее отфильтрованы по publication state и suspension state.

## Public visibility predicates

Portfolio publicly accessible только если:

- User account is active.
- User account is not suspended.
- User account is not `deletion_pending`.
- Portfolio publication state is published.
- Portfolio is not administratively suspended.
- Current `publication_approval_policy` is satisfied, if approval is enabled.

Album publicly accessible только если:

- parent Portfolio is publicly accessible.
- Album publication state is published.
- Album belongs to that Portfolio.

Photo publicly accessible in main Portfolio gallery только если:

- parent Portfolio is publicly accessible.
- Photo publication state is published.
- Photo belongs to that Portfolio.
- Photo is configured to appear in main Portfolio gallery.

Photo publicly accessible through Album только если:

- parent Portfolio is publicly accessible.
- Album is published.
- Photo is published.
- AlbumPhoto connects that Album and Photo.
- Album and Photo belong to same Portfolio.

Listed/unlisted affects discovery, not direct public access. Unpublished Portfolio hides nested Albums and Photos regardless of their individual state. Suspension overrides ordinary publication.

## Required future permission tests

- Owner A cannot list Owner B's photographs.
- Owner A cannot open Owner B's edit URL.
- Owner A cannot update Owner B's photograph by changing a POSTed object ID.
- Owner A cannot delete Owner B's album.
- Owner A cannot use Owner B's image as a cover.
- Owner A cannot forge cover Photo ID outside Album membership.
- Owner A cannot edit Owner B's theme settings.
- Public Visitor cannot see drafts.
- Public Visitor cannot see a suspended portfolio.
- An unverified account cannot upload or create a portfolio.
- A suspended account cannot access owner operations.
- Site Administrator can manage all portfolios.
- Owner A deletion does not affect Owner B.
- Public media URLs controlled by Framehold Engine stop serving deleted assets.
- Deletion retry is safe and does not cross ownership boundaries.
