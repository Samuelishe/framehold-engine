# PERMISSIONS

## Primary MVP roles

- Site Administrator
- Portfolio Owner
- Public Visitor

Возможная будущая роль Collaborator для shared portfolio editing не входит в MVP.

Роли не являются взаимоисключающими. Site Administrator — это permission/capability level, а не отдельный тип человека. Один User может быть Site Administrator и одновременно владеть Portfolio. Ordinary Portfolio Owners are not staff/admin.

## Site Administrator

Global administrator of the whole Framehold Engine installation.

Разрешено:

- manage all users;
- inspect and manage all portfolios;
- suspend or reactivate accounts;
- suspend or hide portfolios;
- manage global site settings;
- manage available themes;
- manage global CMS content;
- access Wagtail Admin;
- perform emergency corrective actions;
- view and edit any portfolio data when required.

## Portfolio Owner

Publicly registered and email-verified user who owns one Portfolio in the MVP.

Разрешено:

- access private Framehold Dashboard;
- edit only own Portfolio;
- choose one available theme;
- configure presentation settings allowed by that theme;
- upload and delete own photographs;
- create and edit own albums;
- change photo order;
- edit titles, captions, alt text, dates and permitted metadata;
- publish and unpublish own content, subject to final publication policy.
- initiate Delete account and all data for their own account and owned data.

Запрещено:

- access another owner's private data;
- edit another portfolio;
- select another owner's media;
- access global settings;
- install or upload theme code;
- receive Wagtail staff/admin access automatically.

## Public Visitor

Разрешено:

- view published portfolios;
- view published albums and photographs;
- open photographs in public viewer/lightbox;
- read author captions and enabled metadata.

Запрещено:

- upload;
- access drafts;
- access private dashboard routes;
- access Wagtail Admin;
- access hidden, suspended or unpublished content.

## Account states and restrictions

- Pending email verification account cannot finish onboarding, create public Portfolio, upload photographs or publish content.
- Suspended account cannot perform owner operations.
- Suspended Portfolio is not public.
- Account deletion removes public access immediately, blocks login/edit/upload operations and revokes active sessions.
- Self-registered users are regular non-staff users.
- The sole Site Administrator account must not be deletable through ordinary Portfolio Owner deletion flow without safe replacement/admin procedure.

## Publication and visibility

- Public queries return only published and non-suspended content.
- Published media may be publicly accessible and saveable.
- A Portfolio may be public but unlisted: direct URL works, but it is omitted from public catalog/index pages.
- Public-but-unlisted is a discoverability setting, not a security boundary.
- Draft/unpublished content is visible only to its Portfolio Owner and Site Administrator through authorized interfaces.
- Hidden/suspended content must not leak through public URL guesses, templates or unrestricted querysets.
- Draft, hidden, suspended and deleted media must not be protected only by absence of links.

## First-publication moderation

Default policy: verified Portfolio Owner may publish independently. Manual approval is not required unless operator configures moderation.

Conceptual setting: `publication_approval_policy`.

Supported MVP values:

- `none` — default; no manual approval required.
- `first_publication` — first transition to public publication requires Site Administrator approval.

Possible `always` moderation is future-only. Approval is not publication. Suspension is not rejection. Publication policy must not be hidden inside theme code or frontend checks.

## Ownership isolation

Подробные invariants и будущие permission tests описаны в `docs/OWNERSHIP_AND_ISOLATION.md`. Короткое правило: UI visibility is not a security boundary; all owner operations must be scoped server-side.
