# DEPLOYMENT

## Статус

Это planned production deployment direction. Production deployment пока не реализован.

Development-only PostgreSQL Compose уже создан в `compose.dev.yml`; это не production Docker infrastructure.

## Базовое направление

- Target: VPS.
- Production OS assumption: Linux, primarily Ubuntu or another Debian-like server distribution.
- Runtime later: Docker Compose.
- Web service for Django/Wagtail application.
- DB service for PostgreSQL 18.
- Reverse proxy through Caddy or Nginx.
- HTTPS through Let's Encrypt.
- Media volume.
- PostgreSQL backup.
- Media backup.
- `.env` or equivalent external secret mechanism.

Windows remains a valid development environment, but production docs, paths, permissions, service assumptions, reverse proxy setup, backups and cron/systemd-like notes should be Linux-oriented. Use POSIX-style paths in deployment docs and avoid backslash-only paths.

## Production email

Production requires:

- SMTP-compatible email delivery;
- credentials from environment variables;
- configured public site origin/domain;
- HTTPS verification links;
- password reset and email verification through the same controlled mail infrastructure.

Email provider is not selected yet.

## Database and driver

Production database direction: PostgreSQL 18 series with Psycopg 3. The foundation starts with `psycopg[binary]` for reliable Windows/Linux development; evaluating another Psycopg 3 variant for production image may happen later without changing domain code.

No SQLite fallback is accepted for production, development or tests.

## Public origin

Registration, verification and password reset links require a configured public origin/domain. `FRAMEHOLD_PUBLIC_ORIGIN` уже присутствует в settings foundation, но реальные account flows и production deployment еще не реализованы.

## Quotas and media operations

Deployment assumptions must account for:

- default storage quota;
- media volume capacity;
- upload size limits;
- backup and restore for both PostgreSQL and media.

Exact quota values remain open.

## Account rate-limit cache

django-allauth rate limits require a real Django cache backend. `DummyCache` is forbidden for account flows. Development/test may use `LocMemCache`; production shared-cache strategy remains open and must be finalized before public production registration. Redis is not required for MVP; database-backed cache may be evaluated.

Client-IP extraction must match actual reverse-proxy topology. Do not trust arbitrary `X-Forwarded-For`; configure allauth proxy settings only after Caddy/Nginx design is known.

## Security and configuration

- Separate development and production secrets.
- No production credentials in Git.
- Review media URL/storage policy before production use.

## Media access boundary

Production deployment must not expose every uploaded source file through a public `/media/` directory by accident. Private-source versus public-delivery media strategy must be selected before real uploads.

Conceptual local filesystem direction:

- `private_media/sources/`
- `public_media/full/`
- `public_media/renditions/`

After account deletion, public delivery assets controlled by Framehold Engine must stop serving. Source originals, generated renditions, thumbnails and cached media under application control must be removed or queued for retryable cleanup according to the final storage design.

Account/media cleanup must account for Linux filesystem permissions. Future Docker Compose production examples target Linux.

## Development Compose distinction

The first development Compose file exists as `compose.dev.yml` with PostgreSQL `db` only. It is not production Docker infrastructure and does not include Django web service, reverse proxy, Redis, mail server or object storage.

## Backup retention and deletion-aware restore

Backups must have documented retention. Restore procedures must reapply known deletion state or otherwise prevent deleted accounts from being resurrected into active service indefinitely.

The project must not promise immediate selective deletion from immutable backups before the final backup mechanism is chosen.

## Operator responsibility

Each deployment operator is responsible for privacy information, Terms of Service, provider disclosure, retention periods, abuse contact, copyright/content complaints and legal operation of their instance.

No external analytics, telemetry, public CDN, font service or phone-home behavior is required for ordinary gallery operation. If operator enables optional external services later, they must be disclosed in operator privacy information.
