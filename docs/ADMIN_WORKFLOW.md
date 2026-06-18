# ADMIN_WORKFLOW

## Статус

Интерфейсы пока не реализованы. Документ фиксирует planned separation between Framehold Dashboard and Wagtail Admin.

## Framehold Dashboard

Framehold Dashboard — core product component, not a future fallback.

Назначение:

- private account area for Portfolio Owners;
- custom Django UI;
- manages only the current owner's Portfolio;
- handles uploads, albums, captions, ordering, theme selection and presentation settings;
- enforces ownership on the server;
- remains understandable for non-technical users;
- does not expose technical Wagtail internals.

## Wagtail Admin

Wagtail Admin reserved for Site Administrator and explicitly trusted staff.

Назначение:

- manage global CMS content;
- manage users and system-level data;
- manage global settings;
- manage available themes metadata/configuration if applicable;
- inspect and correct all portfolios when required;
- perform emergency corrective actions.

Publicly registered user must not automatically receive `is_staff`, `is_superuser`, Wagtail Admin access, global Wagtail collection access or page tree permissions.

## Owner onboarding flow

Planned flow:

1. Visitor registers with email and password.
2. Account remains pending until email verification.
3. Verified user chooses public display name.
4. Verified user chooses Portfolio slug.
5. Verified user selects initial curated theme.
6. Initial Portfolio is created.
7. User enters Framehold Dashboard.

## Portfolio Owner content flow

- Edit Portfolio profile: public name, bio, avatar, cover image.
- Upload photographs within quota and format limits.
- Add title, caption, alt text, captured_at and allowed metadata.
- Create albums.
- Add existing own photos to albums through AlbumPhoto.
- Change album-specific photo order.
- Select theme and configure validated theme settings.
- Preview public presentation.
- Publish/unpublish content subject to final publication policy.
- Open account settings and initiate Delete account and all data.

## Account deletion flow

Framehold Dashboard must provide a clear self-service deletion flow. Ordinary Portfolio Owners must not be required to contact Site Administrator, send manual support email, fill in legal form, or explain a reason.

Deletion and suspension are different operations:

- suspension is reversible and may be performed by Site Administrator;
- deletion is user-initiated hard deletion of active application data after explicit confirmation.

## Site Administrator flow

- Manage users and account states.
- Disable registrations globally if needed.
- Suspend/reactivate accounts.
- Suspend/hide portfolios.
- Review/correct portfolio data when required.
- Manage global homepage/about/contact CMS content.
- Manage global settings such as registration enabled and default quota.

## Publication workflow

Open decision: whether first public publication requires Site Administrator approval. This must be decided before implementing publication states and dashboard publish actions.
