# ROADMAP

## Stage 0: Documentation foundation

Initial documentation foundation.

## Stage 0.5: Product, licensing, and data-lifecycle refinement

- public registration;
- account lifecycle;
- portfolio ownership;
- dashboard boundary;
- theme system;
- media presentation;
- AGPL licensing;
- account deletion and data lifecycle;
- public media saveability policy.

## Stage 0.6: Architecture cleanup before code

- decisions log;
- data model invariants;
- email-only login decision;
- media architecture direction;
- Linux production assumption;
- repository formatting rules.

## Stage 1: Django/Wagtail foundation planning and project initialization

Must establish:

- project package;
- custom User model;
- standard Wagtail Image strategy;
- no permanent migrations before PostgreSQL/dev settings are ready.

Stage 1 and Stage 2 are tightly coupled around custom User, PostgreSQL, settings and first migrations.

## Stage 2: Environment foundation and initial migrations

- split settings;
- PostgreSQL;
- development email backend;
- environment variables;
- first permanent migrations only after custom User is configured.

## Stage 3: Accounts foundation

- public registration;
- mandatory email verification;
- email-only login/logout;
- password reset;
- account states.

## Stage 4: Portfolio domain

- Portfolio;
- Album;
- Photo;
- AlbumPhoto;
- SiteSettings;
- publication states;
- discoverability settings.

## Stage 5: Onboarding, ownership isolation, and moderation

- create first Portfolio after verification;
- owner scoping;
- first-publication approval;
- suspension;
- permission tests;
- deletion isolation tests.

## Stage 6: Framehold Dashboard

- portfolio profile;
- uploads;
- albums;
- photo ordering;
- theme selection;
- presentation settings;
- Delete account and all data flow.

## Stage 7: Private-source/public-delivery media design spike

- verify Wagtail Image/renditions constraints;
- decide source/public storage boundary before real uploads.

## Stage 8: Theme registry and first public theme

- Minimal Justified;
- server-rendered public pages;
- responsive behavior;
- safe public contexts.

## Stage 9: Media presentation

- renditions;
- viewer/lightbox;
- keyboard navigation;
- mobile swipe;
- fullscreen;
- captions and controlled EXIF;
- public full-resolution access.

## Stage 10: Second theme

- Classic Grid;
- theme contract validation;
- focal point/crop workflow if needed.

## Stage 11: Admin usability and public visual polish

Improve Wagtail Admin usability for Site Administrator and polish public presentation after working flows exist.

## Stage 12: Production deployment

- Linux VPS, primarily Ubuntu or Debian-like server;
- Docker Compose;
- reverse proxy;
- HTTPS;
- production email;
- deletion-aware media cleanup;
- operator privacy/legal pages.

## Stage 13: Backup and restore

- PostgreSQL;
- media;
- configuration;
- deletion-aware restore behavior;
- documented backup retention.

## Stage 14: Release governance

- third-party notices audit;
- license and attribution review;
- README/license consistency check;
- bundled asset provenance review.

## Stage 15: Later improvements

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
- optional stronger anti-abuse mechanisms;
- data export before deletion;
- advanced copyright/licensing presentation.
