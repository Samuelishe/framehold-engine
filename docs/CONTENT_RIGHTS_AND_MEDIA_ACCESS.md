# CONTENT_RIGHTS_AND_MEDIA_ACCESS

## Product policy

Framehold Engine is not an anti-copy or DRM-oriented product.

Published photographs are expected to be viewable and saveable by visitors. Framehold Engine must not use fake copy protection:

- do not disable the browser context menu as protection;
- do not use transparent overlays to block saving;
- do not render photographs only through canvas to obscure their source;
- do not deliberately hide image URLs as a security mechanism;
- do not add DRM;
- do not promise that photographs displayed in a browser cannot be copied.

Watermarks are not required by the core product.

## Media asset concepts

### Source original

Private uploaded source file, not served directly by the ordinary public media root. It may contain full EXIF, GPS, editing metadata, original filename concerns, and other private metadata.

### Public full-resolution asset

The highest-quality version intentionally made available to public visitors. It may be generated from the source original, may be metadata-sanitized, and may differ from the raw upload. Exact implementation remains open.

### Public rendition

Resized/cropped formats used in grids, feeds, cards, and the viewer.

Conceptual local filesystem direction:

- `private_media/sources/`
- `public_media/full/`
- `public_media/renditions/`

## Public access direction

A published photograph may expose an explicit Open original or Download original action. A direct URL to a published full-size image is acceptable. Exact original-download controls may be configurable at Portfolio or Photo level later.

The fact that a photograph is downloadable does not grant permission to reuse or redistribute it.

Future UI language should prefer "Open full size" or "Download full size" and avoid implying that the raw uploaded source original is always exposed.

## Security boundary

- Published media may be publicly accessible.
- Draft, hidden, suspended, or deleted media must not become public merely because the storage filename or media URL is known.
- Absence of a link is not an access-control mechanism.
- A public `/media/` directory must not accidentally expose every uploaded source file.
- Private-source versus public-delivery storage strategy must be decided before real upload implementation.
- Security through unguessable filenames alone is not sufficient.
- Raw source-original exposure, if ever allowed, must be an explicit dangerous option with a warning.

## Unresolved implementation options

- Private source storage plus generated public delivery assets.
- Permission-checked media delivery.
- Separate private and public storage backends.
- Publication-time copying or rendition generation.
- Wagtail Image storage constraints and prototype requirements.
- Another reviewed design.

No option is selected in this documentation task.

Before real uploads, create a small technical prototype or architecture spike for standard Wagtail Image, renditions, local filesystem storage and private-source/public-delivery separation.

## EXIF/GPS interaction

Hiding EXIF in the UI does not remove metadata embedded in a downloadable source file. If the raw uploaded source is made public, embedded GPS and other EXIF may also become downloadable.

The final source-original/public-original policy must explicitly address metadata sanitization. Raw GPS must not leak accidentally.

## Copyright and user content

User-uploaded photographs are not automatically licensed under the Framehold Engine software license. Copyright remains with the uploader or other lawful rights holder.

Portfolio Owners must upload only content they have the right to use. The instance needs only the limited operational permission necessary to store, process, resize, and display uploaded content. Exact Terms of Service wording is not drafted here.

Framehold Engine must not claim ownership of user photographs. The future public UI should be able to display a concise copyright/content-rights notice.

## Future tests

- Published public assets are accessible.
- Published full-resolution access follows configured policy.
- Draft assets are not publicly accessible.
- Hidden assets are not publicly accessible.
- Suspended portfolio assets are not publicly accessible.
- Deleted assets are not publicly accessible.
- Another Portfolio Owner cannot access source media through Dashboard.
- UI-hidden EXIF is not assumed to be removed from source files.
- Public templates cannot bypass safe media context.
