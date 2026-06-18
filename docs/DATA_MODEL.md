# DATA_MODEL

## Статус

Это концептуальная модель предметной области. Django models не созданы, миграций нет.

## User

- technical authentication identity;
- custom Django user model from the beginning;
- required unique email;
- email is the preferred login identifier in the initial direction;
- verification and account state handled through established auth mechanisms.

Public Portfolio identity must not depend on authentication username. Public URLs use `Portfolio.slug`, not `User.username`.

MVP cardinality: User has zero or one Portfolio; Portfolio ownership and Site Administrator privileges are not mutually exclusive.

## Portfolio

Принятое решение: `Portfolio` — regular Django domain model, not a Wagtail Page.

Планируемые поля:

- `owner`
- `slug`
- `public_name`
- `bio`
- `avatar`
- `cover_image`
- `theme_key`
- `theme_settings`
- `theme_settings_version`
- `default_caption_visibility`
- `default_capture_date_visibility`
- `default_exif_visibility`
- `publication_state`
- `moderation_state`
- `discoverability`
- `allow_search_indexing`
- possible `original_access_policy`
- `created_at`
- `updated_at`

Назначение: публичная identity и presentation boundary одного Portfolio Owner.

MVP cardinality: Portfolio belongs to exactly one User; one User owns at most one Portfolio.

## Album

Принятое решение: `Album` — regular Django domain model, not a Wagtail Page.

Планируемые поля:

- `portfolio`
- `title`
- `slug`
- `description`
- `cover_photo`
- `publication_state`
- `date_from`
- `date_to`
- `location`
- `sort_order`
- `created_at`
- `updated_at`

## Photo

Принятое решение: `Photo` — Framehold domain model. Initial implementation references the standard Wagtail Image model. Custom Wagtail image model is not planned initially.

Планируемые поля:

- `portfolio`
- `image_asset`
- `title`
- `caption`
- `alt_text`
- `captured_at`
- `exif_data`
- `exif_visibility_override`
- `caption_visibility_override`
- `publication_state`
- `uploaded_by`
- `created_at`
- `updated_at`

Photo belongs to Portfolio, not exclusively to one Album.

MVP cardinality: one Photo corresponds to one Wagtail Image asset. Do not model multiple Photo records pointing to the same Wagtail Image in the MVP.

## AlbumPhoto

Планируемые поля:

- `album`
- `photo`
- `sort_order`
- optional generic `presentation_hint`

Album and Photo use explicit AlbumPhoto relation. One Photo may appear in multiple albums. AlbumPhoto stores album-specific ordering.

## Cardinalities and invariants

- `Portfolio.owner` is unique in MVP.
- `Portfolio.slug` is globally unique, preferably case-insensitive.
- One Portfolio has many Albums; each Album belongs to one Portfolio.
- One Portfolio has many Photos; each Photo belongs to one Portfolio.
- `Album.slug` is unique within Portfolio.
- `AlbumPhoto` is unique per `(album, photo)`.
- `AlbumPhoto.album.portfolio` must match `AlbumPhoto.photo.portfolio`.
- Another owner's Photo must not be usable as an Album cover.
- Another owner's Wagtail Image asset must not be selectable in owner-facing flows.
- Deleting Owner A must not delete or detach Owner B's data.
- Reusing a Photo across albums must not duplicate the underlying image asset.
- Some invariants require server-side validation and tests, not only database constraints.

## State axes

Do not collapse unrelated states into one overloaded `status`.

Conceptual axes:

- User account state: `active`, `email_unverified` or `pending_verification`, `suspended`, `deletion_pending`, `deleted` or physically removed from active data.
- Portfolio publication state: `draft`, `published`, `unpublished`.
- Portfolio moderation state: `pending_approval`, `approved`, `rejected`, `suspended`.
- Discoverability: `listed`, `unlisted`.
- Search indexing preference: `allow_search_indexing` true/false.

Distinctions:

- `suspended` is administrative.
- `unpublished` is owner/publication action.
- `unlisted` means accessible by direct public URL but omitted from public catalog/index pages.
- `allow_search_indexing` is advisory and should affect robots/meta/sitemap behavior later.
- deletion is not suspension.
- approval is not publication.
- publication is not discoverability.

## SiteSettings

Планируемые поля:

- `site_title`
- `site_subtitle`
- `registration_enabled`
- possible `publication_approval_policy`
- `default_storage_quota`
- global homepage configuration
- global about/contact data

## Architectural directions

- User and public Portfolio identity are separate concepts.
- Public URLs must not depend on authentication credentials.
- Theme selection belongs to Portfolio.
- Theme code does not belong in the database.
- Database stores only `theme_key` and validated `theme_settings`.

## Open data model decisions

- Exact publication states.
- Exact public URL scheme: `/photographers/<slug>/`, `/portfolio/<slug>/` or another stable route.
- Exact storage quota and upload size limits.
- Exact representation of email verification state.
- Exact source original / public full-resolution asset / rendition representation.
- Email and public slug reuse after deletion.
