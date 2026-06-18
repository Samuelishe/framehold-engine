# DEPLOYMENT

## Статус

Это planned deployment direction. Ничего из перечисленного пока не реализовано.

## Базовое направление

- Target: VPS.
- Runtime later: Docker Compose.
- Web service for Django/Wagtail application.
- DB service for PostgreSQL.
- Reverse proxy through Caddy or Nginx.
- HTTPS through Let's Encrypt.
- Media volume.
- PostgreSQL backup.
- Media backup.
- `.env` or equivalent external secret mechanism.

## Production email

Production requires:

- SMTP-compatible email delivery;
- credentials from environment variables;
- configured public site origin/domain;
- HTTPS verification links;
- password reset and email verification through the same controlled mail infrastructure.

Email provider is not selected yet.

## Public origin

Registration, verification and password reset links require a configured public origin/domain. This is planned, not implemented.

## Quotas and media operations

Deployment assumptions must account for:

- default storage quota;
- media volume capacity;
- upload size limits;
- backup and restore for both PostgreSQL and media.

Exact quota values remain open.

## Security and configuration

- Separate development and production secrets.
- No production credentials in Git.
- Review media URL/storage policy before production use.

## Media access boundary

Production deployment must not expose every uploaded source file through a public `/media/` directory by accident. Private-source versus public-delivery media strategy must be selected before real uploads.

After account deletion, public delivery assets controlled by Framehold Engine must stop serving. Source originals, generated renditions, thumbnails and cached media under application control must be removed or queued for retryable cleanup according to the final storage design.

## Backup retention and deletion-aware restore

Backups must have documented retention. Restore procedures must reapply known deletion state or otherwise prevent deleted accounts from being resurrected into active service indefinitely.

The project must not promise immediate selective deletion from immutable backups before the final backup mechanism is chosen.

## Operator responsibility

Each deployment operator is responsible for privacy information, Terms of Service, provider disclosure, retention periods, abuse contact, copyright/content complaints and legal operation of their instance.
