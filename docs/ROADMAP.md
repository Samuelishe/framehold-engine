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

## Stage 1: Technical foundation implementation — implemented

- initialized uv application project;
- created `pyproject.toml`;
- created `uv.lock`;
- created `.python-version`;
- installed selected runtime/dev dependencies;
- scaffolded/adapted Django/Wagtail foundation;
- created `apps.accounts` custom User;
- created minimal `apps.sitecontent` for Wagtail root/global CMS;
- configured Wagtail Admin.

Selected foundation stack: CPython 3.14, Django 5.2 LTS, Wagtail 7.4 LTS, django-allauth regular accounts, django-environ, PostgreSQL 18, Psycopg 3, Ruff and pytest.

Stage 1 and Stage 2 are tightly coupled around custom User, PostgreSQL, settings and first migrations.

## Stage 2: Environment foundation and initial migrations — implemented

- split settings: `base/dev/test/prod`;
- django-environ;
- `.env.example`;
- PostgreSQL 18 via `compose.dev.yml`;
- Psycopg 3;
- development console email backend;
- test settings;
- first PostgreSQL migrations after custom User was configured;
- email-based superuser validation;
- Wagtail Admin smoke test;
- Ruff/pytest checks.

Stage 1 and Stage 2 were implemented in one tightly scoped task because migration ordering crossed both stages.

## Stage 3: Accounts foundation

- django-allauth account-flow implementation;
- registration pages;
- mandatory email verification UX;
- public registration;
- email-only login/logout;
- password reset;
- account states;
- account tests.

## Stage 4: Portfolio domain

- Portfolio;
- Album;
- Photo;
- AlbumPhoto;
- SiteSettings;
- publication states;
- discoverability settings.

## Stage 5: Onboarding, ownership isolation, optional moderation, and public visibility predicates

- create first Portfolio after verification;
- owner scoping;
- optional first-publication approval;
- public visibility predicates;
- suspension;
- permission tests;
- deletion isolation tests.

## Stage 6: Private-source/public-delivery media design spike

- verify Wagtail Image/renditions constraints;
- decide source/public storage boundary before real uploads.

## Stage 7: Theme registry foundation and built-in default theme

- `minimal_justified`;
- safe default and fallback behavior;
- theme settings versioning;
- preview direction;
- safe rendering contract.

## Stage 8: Framehold Dashboard

- portfolio profile;
- Photo management and upload after media design is accepted;
- Album management;
- Portfolio gallery ordering;
- theme selection;
- preview;
- presentation settings;
- Delete account and all data flow.

## Stage 9: First public theme and public routes

- Minimal Justified;
- `/portfolio/<slug>/`;
- Album route;
- listed/unlisted behavior;
- safe public contexts.

## Stage 10: Media presentation

- renditions;
- viewer/lightbox;
- keyboard navigation;
- mobile swipe;
- fullscreen;
- captions and controlled EXIF;
- public full-resolution access.

## Stage 11: Second theme and visual refinement

- Classic Grid;
- focal point/crop behavior;
- theme contract validation;

## Stage 12: Admin usability and public visual polish

Improve Wagtail Admin usability for Site Administrator and polish public presentation after working flows exist.

## Stage 13: Production deployment

- Linux VPS, primarily Ubuntu or Debian-like server;
- Docker Compose;
- reverse proxy;
- HTTPS;
- production email;
- deletion-aware media cleanup;
- operator privacy/legal pages.

## Stage 14: Backup and restore

- PostgreSQL;
- media;
- configuration;
- deletion-aware restore behavior;
- documented backup retention.

## Stage 15: Release governance

- third-party notices audit;
- license and attribution review;
- README/license consistency check;
- bundled asset provenance review.

## Stage 16: Later improvements

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
