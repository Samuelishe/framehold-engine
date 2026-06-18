# ACCOUNT_DELETION_AND_DATA_LIFECYCLE

## Статус

Complete account deletion is a core product requirement. Реализации пока нет.

User-facing action: **Delete account and all data**.

Это должен быть понятный self-service flow во Framehold Dashboard settings. "One button" означает один ясный пользовательский сценарий, а не необратимое удаление по случайному клику.

## Planned UX flow

1. Portfolio Owner открывает account settings.
2. Portfolio Owner выбирает Delete account and all data.
3. System clearly lists what will be deleted.
4. User re-authenticates or confirms through a sufficiently recent authenticated session.
5. User performs explicit irreversible confirmation.
6. Account enters deletion processing.
7. Public access to the portfolio is removed immediately.
8. Existing sessions and authentication tokens are revoked.
9. All owned data is deleted.
10. User receives clear completion or pending-deletion result.

Не требуется: звонить администратору, писать manual support email, заполнять legal form или объяснять reason for deletion.

## Deletion scope

Deletion conceptually includes:

- User account;
- email address and profile fields;
- email-verification records;
- password-reset records or tokens where applicable;
- active sessions;
- Portfolio;
- avatar;
- cover image;
- theme selection;
- theme settings;
- Albums;
- Photos;
- AlbumPhoto relations;
- source originals;
- public full-resolution assets;
- generated renditions;
- thumbnails;
- cached media under application control;
- captions;
- alt text;
- EXIF data stored by Framehold Engine;
- upload metadata;
- account preferences;
- other owner-created records.

Deletion must not affect another user's account, portfolio, media, or unrelated global application content.

## Architectural requirements

- Deletion is a hard-deletion workflow for active application data.
- Do not keep an indefinite soft-deleted copy of the complete account.
- Account suspension and account deletion are different operations.
- Suspension is reversible.
- Deletion is irreversible after the confirmation boundary.
- Database cascading alone is not enough because filesystem/object-storage files and renditions must also be removed.
- Deletion processing must be idempotent.
- Retry must not corrupt unrelated data.
- Partial failure must be detectable.
- Failed file cleanup must be retryable.
- Deletion must not leave orphaned originals or renditions.
- Public routes must stop serving the deleted portfolio.
- Direct public media URLs controlled by Framehold Engine must stop serving deleted assets.
- Deletion implementation must be covered by integration tests later.

## Immediate behavior after confirmation

- Portfolio becomes unavailable publicly.
- Login is blocked.
- Upload and editing operations are blocked.
- Sessions are invalidated.
- Deletion cleanup may finish synchronously or through a later background/reconciliation mechanism.
- No job system such as Celery is selected in this documentation task.

## Backups and restore

- Active-system deletion and backup expiration are separate concerns.
- Backups must have a documented retention period.
- Deleted personal data must not be restored into active service indefinitely.
- Restore procedures must reapply known deletion state or otherwise prevent resurrection of deleted accounts.
- Backup handling must be documented before production deployment.
- Do not promise immediate selective deletion from every immutable backup before the backup mechanism is chosen.
- The project must not claim full legal compliance merely because a delete button exists.

## Logs and external processors

- Operational/security logs must minimize personal data.
- Log-retention periods must be documented.
- Logs must not become a hidden permanent copy of deleted profile data.
- SMTP/email providers may retain their own delivery metadata.
- VPS providers, object-storage providers, monitoring services, and backup services may act as external processors.
- Each deployment operator must disclose relevant retention and providers in their own privacy information.

## Special cases

- The sole Site Administrator account must not be deletable through the ordinary Portfolio Owner flow without a safe replacement/admin procedure.
- Future shared portfolios or collaborator roles require ownership-transfer rules.
- Email and public-slug reuse after deletion remain open decisions.
- Optional data export before deletion may be considered later.

## Legal wording

The feature supports data-erasure and data-lifecycle requirements. It does not automatically guarantee compliance with GDPR or every jurisdiction. The right to erasure is not absolute in every legal situation. Each self-hosted operator remains responsible for legal operation of their instance.

## Future tests

- Owner can start deletion only while authenticated.
- Re-authentication or recent-session confirmation is required.
- CSRF-protected request is required.
- Deletion immediately unpublishes the portfolio.
- Existing sessions become invalid.
- User cannot log in after deletion begins.
- Portfolio is removed.
- Albums are removed.
- Photos are removed.
- AlbumPhoto relations are removed.
- Wagtail Image assets owned exclusively by the portfolio are removed according to final ownership rules.
- Originals are removed.
- Renditions are removed.
- Avatars and cover media are removed.
- Owner A deletion does not affect Owner B.
- Retrying deletion is safe.
- Partial cleanup can be resumed.
- Public portfolio URL stops working.
- Public media URLs controlled by Framehold Engine stop working.
- Sole Site Administrator protection works.
