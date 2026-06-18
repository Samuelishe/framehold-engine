# DATA_MODEL

## Статус

Это концептуальная модель предметной области. Django models не созданы, миграций нет.

## User

- technical authentication identity;
- custom Django user model from the beginning;
- required unique email;
- verification and account state handled through established auth mechanisms.

Public Portfolio identity must not depend on authentication username. Public URLs use `Portfolio.slug`, not `User.username`.

## Portfolio

Планируемые поля:

- `owner`
- `slug`
- `public_name`
- `bio`
- `avatar`
- `cover_image`
- `theme_key`
- `theme_settings`
- `default_caption_visibility`
- `default_capture_date_visibility`
- `default_exif_visibility`
- `publication_state`
- `suspension_state`
- `created_at`
- `updated_at`

Назначение: публичная identity и presentation boundary одного Portfolio Owner.

## Album

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

## AlbumPhoto

Планируемые поля:

- `album`
- `photo`
- `sort_order`
- optional generic `presentation_hint`

Album and Photo use explicit AlbumPhoto relation. One Photo may appear in multiple albums. AlbumPhoto stores album-specific ordering.

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

### Portfolio and Album representation

Unresolved:

- regular Django models;
- Wagtail Page models;
- hybrid approach.

Wagtail Pages offer revisions and publishing. Regular Django models may simplify self-service ownership isolation and dashboard workflows. This must be decided explicitly before implementation.

### Image representation

Unresolved:

- default Wagtail Image plus Framehold Photo model;
- custom Wagtail image model;
- another controlled image asset model.

Changing Wagtail's image model after real migrations/data may be difficult, so this decision must be reviewed before permanent migration history.

### Other open decisions

- Exact publication states.
- Whether first public publication requires Site Administrator approval.
- Exact public URL scheme: `/photographers/<slug>/`, `/portfolio/<slug>/` or another stable route.
- Exact storage quota and upload size limits.
- Exact representation of email verification state.
