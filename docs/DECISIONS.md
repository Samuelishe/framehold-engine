# DECISIONS

Компактный журнал принятых архитектурных решений Framehold Engine. Подробности остаются в topic docs.

## DEC-001 — Custom Django User before initial migrations

- Статус: Accepted.
- Дата или этап: Stage 1.
- Контекст: менять `AUTH_USER_MODEL` после реальных миграций и данных сложно.
- Решение: Framehold Engine использует custom Django User model с самого начала, до первых постоянных application migrations.
- Последствия: custom User должен быть установлен во время Stage 1.
- Supersedes / Superseded by: none.

## DEC-002 — Email-only login as preferred initial direction

- Статус: Accepted as initial direction.
- Дата или этап: Stage 0.6.
- Контекст: публичная identity принадлежит Portfolio, а не authentication credentials.
- Решение: использовать email как login identifier. Не показывать и не требовать public username в MVP. Public identity использует `Portfolio.slug` и `Portfolio.public_name`.
- Последствия: регистрация проще, путаница username/portfolio slug устраняется, exact auth package остается открытым.
- Supersedes / Superseded by: supersedes email plus internal username as equal initial direction.

## DEC-003 — Portfolio and Album are regular Django models

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: public self-service dashboard и ownership scoping являются core requirements.
- Решение: Portfolio и Album являются regular Django domain models, not Wagtail Pages, в принятой initial architecture.
- Последствия: Framehold Dashboard и server-side ownership scoping остаются проще. Wagtail остается полезным для admin/CMS infrastructure, images, settings и global staff workflows.
- Supersedes / Superseded by: supersedes open Page-versus-model decision for initial architecture.

## DEC-004 — Photo references standard Wagtail Image

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: image infrastructure должна переиспользовать Wagtail там, где это полезно, без переноса domain rules в Wagtail Image.
- Решение: Photo является Framehold domain model и initially references the standard Wagtail Image model. Custom Wagtail image model не входит в initial implementation.
- Последствия: Wagtail renditions/focal points/image infrastructure можно переиспользовать. Ownership, captions, EXIF, publication и portfolio-specific rules остаются в Framehold domain models.
- Supersedes / Superseded by: supersedes custom Wagtail image model as initial strategy.

## DEC-005 — One Photo corresponds to one Wagtail Image asset in MVP

- Статус: Accepted for MVP.
- Дата или этап: Stage 0.6.
- Контекст: media lifecycle, ownership и deletion должны оставаться простыми в MVP.
- Решение: domain Photo должен иметь one-to-one relationship with a Wagtail Image asset в MVP. Reuse across albums выполняется через AlbumPhoto, а не через несколько Photo records, указывающих на один Wagtail Image.
- Последствия: упрощаются ownership, deletion, cleanup, EXIF и media lifecycle.
- Supersedes / Superseded by: none.

## DEC-006 — Framehold Dashboard is separate from Wagtail Admin

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: publicly registered Portfolio Owners нужен private non-technical UI.
- Решение: Framehold Dashboard является ordinary private UI для Portfolio Owners. Wagtail Admin зарезервирован для Site Administrator и explicitly trusted staff.
- Последствия: self-registered users никогда не получают Wagtail staff/admin access автоматически.
- Supersedes / Superseded by: supersedes Wagtail Admin as ordinary contributor interface.

## DEC-007 — Published images are saveable; no fake DRM

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: browser-visible images нельзя надежно защитить от копирования.
- Решение: published photographs intentionally viewable/saveable. Framehold Engine не использует fake copy protection, context-menu blocking, transparent overlays, canvas-only hiding или DRM.
- Последствия: media security фокусируется на защите unpublished/deleted/suspended content, а не на притворстве, что browser-visible images нельзя скопировать.
- Supersedes / Superseded by: none.

## DEC-008 — Private source and public delivery are separate media concepts

- Статус: Accepted as architectural direction, implementation unresolved.
- Дата или этап: Stage 0.6.
- Контекст: raw uploads могут содержать private metadata и не должны автоматически равняться public assets.
- Решение: различать private source originals, public full-resolution assets и public renditions. Exact storage/delivery implementation остается открытым.
- Последствия: metadata sanitization и draft-media protection нужно спроектировать до real uploads.
- Supersedes / Superseded by: none.

## DEC-009 — Curated themes only in MVP

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: arbitrary user theme code — высокий риск для security и quality.
- Решение: themes являются trusted code-defined presets, shipped with Framehold Engine. Portfolio Owners могут выбирать installed themes и safe settings, но не могут upload arbitrary HTML/CSS/JS/template code в MVP.
- Последствия: улучшаются security и visual quality. User-authored/external themes остаются future-only и требуют separate architecture review.
- Supersedes / Superseded by: none.

## DEC-010 — AGPL-3.0-or-later

- Статус: Accepted.
- Дата или этап: Stage 0.5.
- Контекст: Framehold Engine — server software, который должен оставаться free and open-source.
- Решение: Framehold Engine licensed under GNU Affero General Public License v3.0 or later.
- Последствия: software license отделен от user-content rights и third-party material licenses.
- Supersedes / Superseded by: none.

## DEC-011 — Linux VPS production assumption

- Статус: Accepted as deployment assumption.
- Дата или этап: Stage 0.6.
- Контекст: production hosting для Django/Wagtail/VPS deployments ожидаемо Linux-oriented.
- Решение: production hosting expected to run on Linux in almost all cases, typically Ubuntu or a similar Debian-like server distribution.
- Последствия: deployment docs, paths, service assumptions, scripts, reverse proxy setup, permissions, backup и runtime examples должны быть Linux-oriented. Windows остается supported development environment, но не main production target.
- Supersedes / Superseded by: none.
