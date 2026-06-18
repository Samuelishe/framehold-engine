# Framehold Engine

A self-hosted, multi-user photo portfolio engine built around curated themes and owner-controlled galleries.

## Overview

Framehold Engine is a self-hosted web gallery engine where one installation is intended to host multiple independent public photography portfolios.

Users will register publicly, verify their email address, create one portfolio in the MVP, choose a curated theme, upload photographs through the private Framehold Dashboard, create albums, configure presentation options, and publish public portfolio pages.

Public visitors see published portfolios, albums, and photographs. Site Administrators use Wagtail Admin for global administration, trusted staff tasks, global CMS content, and emergency corrections. The public frontend is custom, server-rendered, and theme-driven.

## Project Status

Framehold Engine is pre-alpha. The Stage 1/2 technical foundation now exists.

The repository contains a minimal Django/Wagtail foundation with uv metadata, locked dependencies, split settings, a custom email-only User model, django-allauth foundation configuration, PostgreSQL development Compose, initial PostgreSQL migrations, a minimal Wagtail homepage/admin, Ruff, and pytest.

There is no production-ready release. Registration UX, Portfolio models, Framehold Dashboard, public portfolio pages, themes, media uploads, and account deletion are not implemented yet. Features described in the documentation are planned unless explicitly marked as implemented.

## Product Direction

The planned product includes:

- curated portfolio themes;
- responsive public portfolio layouts;
- albums and reusable photos;
- author captions;
- controlled EXIF display;
- lightbox/fullscreen viewing;
- viewable and saveable published images;
- owner-controlled account deletion and data lifecycle.

Framehold Engine is portfolio-oriented, not social-network-oriented.

## What Framehold Engine Is Not

Framehold Engine is not a social network. The MVP does not include likes, follows, visitor comments, direct messages, public activity feeds, ratings, public anonymous uploads, or mandatory social sharing buttons.

Framehold Engine is also not a DRM or anti-copy product. It does not promise that photographs displayed in a browser cannot be saved or copied. It is not a hosted commercial SaaS product.

## Planned Architecture

The foundation stack is:

- Python 3.14;
- Django 5.2 LTS;
- Wagtail 7.4 LTS;
- PostgreSQL 18;
- Psycopg 3;
- uv with `pyproject.toml` and `uv.lock`;
- custom Django User model without `username`;
- django-allauth account foundation;
- Ruff and pytest.

The planned product architecture still includes:

- Portfolio and Album as regular Django domain models;
- Photo as a Framehold domain model referencing the standard Wagtail Image model initially;
- server-rendered public frontend;
- Tailwind CSS;
- Alpine.js or HTMX for limited interactivity;
- PhotoSwipe or another reviewed viewer/lightbox;
- Docker Compose later;
- local media storage first, with possible S3-compatible storage later.

Unresolved implementation details are documented in the architecture docs.

## Development Setup

This project currently uses Python 3.14, uv, Docker Compose, and PostgreSQL 18.

Prepare dependencies:

```powershell
uv sync --locked
```

Create a local environment file from the safe example and set development-only values:

```powershell
Copy-Item .env.example .env
```

Start the development database:

```powershell
docker compose -f compose.dev.yml up -d db
```

Run migrations:

```powershell
uv run python manage.py migrate
```

Run checks and tests:

```powershell
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Start the development server:

```powershell
uv run python manage.py runserver
```

Stop the development database without deleting the named volume:

```powershell
docker compose -f compose.dev.yml down
```

## Account and Privacy Principles

Public registration requires email verification before portfolio onboarding, uploads, or publishing. Portfolio ownership isolation must be enforced server-side.

Framehold Engine must support a self-service "Delete account and all data" flow that removes owned active application data, revokes sessions, and stops public access to the portfolio. Backup retention, restore behavior, logs, external processors, and privacy notices remain operator responsibilities.

The software can support data-erasure workflows, but it does not automatically guarantee legal compliance for every jurisdiction or deployment.

## Media Philosophy

Published photographs are intentionally viewable and saveable by visitors. Framehold Engine does not use fake copy protection, browser-context-menu blocking, transparent overlays, canvas-only rendering to hide image URLs, or DRM.

Unpublished, hidden, suspended, or deleted media must remain protected by real access-control and storage design. User content remains owned by its rights holders. Downloading a public photograph does not grant permission to reuse or redistribute it.

## Documentation

Detailed project documentation is in Russian:

- [Documentation map](docs/README.md)
- [Project state](docs/PROJECT_STATE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical foundation](docs/TECHNICAL_FOUNDATION.md)
- [Data model](docs/DATA_MODEL.md)
- [Registration and accounts](docs/REGISTRATION_AND_ACCOUNTS.md)
- [Ownership and isolation](docs/OWNERSHIP_AND_ISOLATION.md)
- [Account deletion and data lifecycle](docs/ACCOUNT_DELETION_AND_DATA_LIFECYCLE.md)
- [Theme system](docs/THEME_SYSTEM.md)
- [Media presentation](docs/MEDIA_PRESENTATION.md)
- [Content rights and media access](docs/CONTENT_RIGHTS_AND_MEDIA_ACCESS.md)
- [Open-source and third-party policy](docs/OPEN_SOURCE_AND_THIRD_PARTY_POLICY.md)
- [Privacy and operator responsibilities](docs/PRIVACY_AND_OPERATOR_RESPONSIBILITIES.md)

## License

Framehold Engine is free and open-source software licensed under the [GNU Affero General Public License version 3 or later](LICENSE).

SPDX identifier: `AGPL-3.0-or-later`.

The official project is distributed at no charge. The license permits use, modification, redistribution, hosting, and commercial activity subject to AGPL requirements. Modified versions made available to users over a network must comply with the AGPL source-availability requirements.

Framehold Engine is provided as-is, without warranty, to the extent permitted by applicable law. See [LICENSE](LICENSE) for the actual license terms.

## Third-party Acknowledgements

Third-party components and assets retain their own licenses. The project inventory and attribution policy are tracked in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Direct runtime dependencies and development tools are listed in `THIRD_PARTY_NOTICES.md`. Third-party components retain their own licenses.

## User Content

User-uploaded photographs, captions, biographies, avatars, and portfolio text are not automatically licensed under AGPL. Uploaders must have the necessary rights to the content they publish. Copyright remains with the relevant rights holder.

Framehold Engine needs only the operational permission required for a deployed instance to store, process, resize, and display uploaded content according to that instance's terms and settings.

## Repository Safety

Do not commit secrets, `.env` files, database dumps, private keys, production credentials, real private media, or real private personal data.
