# SECURITY_NOTES

## Минимальные правила безопасности

- No secrets in Git.
- No `.env` commits.
- No DB dumps in Git.
- No private keys in Git.
- No private media in Git.
- Use Django password hashing.
- Use Django sessions.
- Use established auth/verification mechanisms.
- No custom authentication protocol.
- No custom token cryptography.
- Development and production secrets must be separated.
- Obscurity of media URLs is not authorization.

## Registration and verification

- Email required and unique case-insensitively.
- Email normalized consistently.
- Email-only login is the preferred initial direction.
- Verification links expire and are single-use.
- Resend verification has cooldown.
- Signup, login, verification resend and password reset must be rate-limited.
- Account-sensitive forms must not unnecessarily reveal whether an email exists.
- Password reset uses verified email channel.
- Registration never grants Wagtail Admin access automatically.
- Administrator can disable new registrations globally.
- Default publication approval policy is `none`; optional first-publication moderation may be enabled by operator.

Email verification confirms control of a mailbox and prevents repeated registration with the same unique email. It does not prove that one physical person owns only one account and does not prevent deliberate registration with multiple email addresses.

MVP security remains proportional. CAPTCHA, Turnstile, SMS, mandatory 2FA, social login, identity documents and enterprise identity providers are not required for MVP.

## Ownership and permissions

- Portfolio Owner must not edit another Portfolio.
- Owner-facing querysets must be scoped server-side.
- UI visibility is not a security boundary.
- Forged form IDs must not select another owner's objects.
- Public queries return only published and non-suspended content.
- Suspended accounts cannot perform owner operations.
- Self-registered users are non-staff by default.

## Upload safety

- Uploads only for verified authenticated Portfolio Owners.
- Anonymous uploads forbidden.
- Allowed image formats explicitly defined.
- Extension alone is not trusted.
- Image content decoded/validated by established libraries.
- Maximum file size and decompression/pixel limits required.
- Per-account or per-portfolio quota required.
- Failed/partial uploads must not create broken public entries.
- Draft/hidden media is not private merely because no public page links to it.
- Media URL/storage policy must be reviewed separately.
- Public `/media/` must not accidentally expose every uploaded source file.
- Source original, public full-resolution asset and public rendition are separate concepts.
- Raw source originals are private uploaded files and are not served directly by ordinary public media root.
- Public full-resolution assets may differ from raw upload and may be metadata-sanitized.

## EXIF and metadata

- Raw EXIF JSON must not be rendered publicly.
- Public EXIF uses allowlist.
- GPS coordinates are not displayed by default.
- EXIF visibility is opt-in or explicitly configurable.
- Hiding EXIF in UI does not strip metadata embedded in downloadable source files.

## Account deletion security

- Phase 1 requires authentication, destructive confirmation and CSRF protection.
- Phase 1 sets account to `deletion_pending`, removes public access, blocks login/upload/editing and revokes sessions/tokens.
- Phase 2 performs idempotent cleanup of media, domain data, account records and final User identity.
- User and ownership records must not be permanently removed before cleanup has enough information to identify owned files.
- Missing files are treated as already removed.
- Partial cleanup must be detectable and retryable.
- Destructive querysets must be explicitly scoped to the deleting owner.
- Cleanup architecture must not depend on Celery.

## Themes

- No user-uploaded theme packages in MVP.
- No arbitrary template execution.
- No arbitrary JavaScript injection.
- No arbitrary CSS injection.
- Themes receive only prepared and safely filtered public context.
- Themes cannot control authorization, ownership, authentication or publication policy.

## Public media and no DRM

Published photographs may be publicly accessible and saveable. Do not use fake DRM, context-menu blocking, overlays, canvas-only rendering or URL hiding as security mechanisms.

## Owner-authored text

Portfolio Owner-authored content is plain text in MVP. No owner-supplied HTML, raw Markdown rendering or rich-text editor. Django template autoescaping must not be disabled. EXIF strings and filenames are untrusted text. Theme templates must not mark owner content safe.

## No mandatory telemetry

Core Framehold Engine and built-in themes must not require telemetry, analytics, project phone-home services, external fonts, public CDN JavaScript or tracking by default. Optional external services require explicit operator configuration and privacy disclosure.

## Runtime assumptions

Production security guidance should assume Linux VPS, typically Ubuntu or Debian-like server. Avoid relying on case-insensitive filesystem behavior, Windows-specific paths or backslash-only paths.
