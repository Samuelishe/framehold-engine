# OPEN_SOURCE_AND_THIRD_PARTY_POLICY

## Project license

Framehold Engine is free and open-source software licensed under GNU Affero General Public License version 3 or later.

SPDX identifier: `AGPL-3.0-or-later`.

The official project is distributed at no charge. This does not mean commercial use is forbidden. The license permits use, modification, redistribution, hosting, and commercial activity subject to AGPL requirements.

AGPL was selected because Framehold Engine is server software. Modified versions made available to users over a network must comply with the AGPL source-availability requirements. The actual terms are in the root `LICENSE` file.

Framehold Engine is provided as-is, without warranty, to the extent permitted by applicable law.

## What AGPL applies to

AGPL-3.0-or-later applies to:

- Framehold Engine source code;
- project-authored application templates;
- project-authored styles and scripts;
- project-authored documentation, subject to repository policy;
- project-authored theme code and assets, unless another license is explicitly stated.

## What AGPL does not automatically apply to

AGPL does not automatically apply to:

- user-uploaded photographs;
- user captions;
- user biographies;
- user avatars;
- user portfolio text;
- third-party fonts;
- third-party icons;
- third-party demo assets;
- third-party dependencies.

## Third-party notice policy

The canonical project `LICENSE` must not be used as a third-party notice list. `THIRD_PARTY_NOTICES.md` is the human-readable source of truth for intentionally included or adapted third-party components and assets.

At the documentation-only stage there may be no bundled dependencies or assets. Do not pretend planned technologies are already vendored. Do not invent authors, versions, URLs or license identifiers.

## Software policy

- Only free and open-source software may be intentionally included as a project dependency.
- Each dependency license must be reviewed for compatibility with Framehold Engine's intended AGPL distribution.
- OSI-approved licenses are preferred, but approval alone does not automatically prove compatibility.
- No source-available-but-non-open dependency should be added silently.
- No proprietary runtime dependency should be added without an explicit project-level decision.
- Do not remove upstream copyright or license headers.
- Vendored code must preserve notices.
- Lockfiles and dependency metadata must remain committed when introduced.
- Future dependency changes must update `THIRD_PARTY_NOTICES.md` when relevant.

## Content and visual-asset policy

Allowed only after license verification:

- original project-created content;
- public-domain material;
- CC0 material;
- CC BY material with attribution;
- CC BY-SA material when compatible with intended use;
- freely licensed fonts such as appropriately licensed OFL fonts;
- open-source icon sets with preserved attribution;
- other genuinely free/open content licenses reviewed case by case.

Do not accept silently:

- assets with no license;
- "free download" assets without reuse terms;
- copied portfolio screenshots;
- copied commercial website templates;
- stock photographs without redistribution rights;
- proprietary fonts;
- non-commercial-only assets;
- no-derivatives assets when adaptation or redistribution is required;
- content copied only because it is publicly visible on the web.

## No mandatory external asset services

Built-in themes and core public UI should serve project assets locally, use locally bundled and properly licensed fonts/icons where needed, or use suitable system font stacks.

They must not require Google Fonts, another third-party font service, public CDN JavaScript, analytics, trackers or communication with project-operated infrastructure.

Operator-configured optional external services may be added later only as explicit choices and must be documented in operator privacy information.

## Reference screenshots

Screenshots previously used during architecture discussion are visual references only. They must not be added to the repository or shipped with Framehold Engine unless license and redistribution rights are independently verified.

Do not copy logos, photographs, fonts, code, or exact visual assets from references. Theme implementations may take general layout inspiration but must be independently implemented.

## Future audit process

Before a release, verify:

- root `LICENSE` exists and is canonical AGPL v3 text;
- README states SPDX `AGPL-3.0-or-later`;
- `THIRD_PARTY_NOTICES.md` is current;
- bundled third-party license texts are present when required;
- no unlicensed assets are shipped;
- source headers and notices are preserved.
