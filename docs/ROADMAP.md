# ROADMAP

## Stage 0: Documentation foundation

Create the initial documentation foundation.

## Stage 0.5: Product refinement

- public registration;
- account lifecycle;
- portfolio ownership;
- dashboard boundary;
- theme system;
- media presentation.
- licensing and data-lifecycle refinement;
- public media saveability policy.

## Stage 1: Django/Wagtail foundation

Before permanent initial migrations:

- establish custom User model;
- use standard Wagtail Image strategy for initial Framehold Photo;
- keep Portfolio and Album as regular Django domain models.

## Stage 2: Environment foundation

- split settings;
- PostgreSQL;
- development email backend;
- environment variables.

## Stage 3: Accounts

- public registration;
- mandatory email verification;
- login/logout;
- password reset;
- account states;
- onboarding.
- account deletion entry point and confirmation flow.

## Stage 4: Portfolio domain

- Portfolio;
- Album;
- Photo;
- AlbumPhoto;
- SiteSettings;
- publication states.

## Stage 5: Ownership isolation

- server-side scoping;
- account/portfolio boundaries;
- suspension;
- permission tests.
- deletion isolation tests.
- private/public media delivery design before real uploads.

## Stage 6: Framehold Dashboard

- portfolio profile;
- uploads;
- album management;
- photo ordering;
- theme selection;
- presentation settings.
- Delete account and all data flow.

## Stage 7: Theme registry and first public theme

- Minimal Justified;
- server-rendered public pages;
- responsive behavior.

## Stage 8: Media presentation

- renditions;
- viewer/lightbox;
- keyboard navigation;
- mobile swipe;
- fullscreen;
- captions and controlled EXIF.
- public full-resolution access policy.
- source original/public delivery boundary.

## Stage 9: Second theme

- Classic Grid;
- theme contract validation;
- focal point/crop workflow if needed.

## Stage 10: Admin usability and public visual polish

Improve Wagtail Admin usability for Site Administrator and polish public presentation after working flows exist.

## Stage 11: Production deployment

- Docker Compose;
- reverse proxy;
- HTTPS;
- production email.
- deletion-aware media cleanup;
- operator privacy/legal pages.

## Stage 12: Backup and restore

- PostgreSQL;
- media;
- configuration.
- deletion-aware restore behavior.
- documented backup retention.

## Stage 12.5: Release governance

- third-party notices audit;
- license and attribution review;
- README/license consistency check;
- bundled asset provenance review.

## Stage 13: Later improvements

- Nocturne Mosaic;
- Journal Feed;
- tags;
- search;
- private albums;
- password-protected albums;
- advanced EXIF;
- S3-compatible storage;
- Cloudflare R2;
- analytics;
- multilingual support;
- collaborators;
- optional stronger anti-abuse mechanisms.
- data export before deletion.
- advanced copyright/licensing presentation.
