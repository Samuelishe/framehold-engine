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
