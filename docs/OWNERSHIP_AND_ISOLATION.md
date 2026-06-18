# OWNERSHIP_AND_ISOLATION

## Статус

Ownership isolation — hard requirement для multi-portfolio Framehold Engine. Это не обязательно enterprise SaaS multitenancy, но серверная изоляция портфолио обязательна.

## MVP ownership model

- One verified user account owns one Portfolio.
- One Portfolio belongs to exactly one Portfolio Owner.
- One-account-one-portfolio limitation may be relaxed later.
- Site Administrator may manage all portfolios.

## Server-side invariants

- Every owner-facing queryset must be scoped to the authenticated owner's portfolio.
- Object visibility in the UI is not a security boundary.
- Direct access to another owner's edit/delete URL must be rejected.
- Forged form IDs must not allow selecting another owner's objects.
- Another owner's image must not be usable as an album cover.
- Another owner's theme settings must not be editable.
- Another owner's unpublished content must never appear in dashboard queries.
- Public queries must return only published and non-suspended content.
- Templates must not query unrestricted global `Photo` or `Album` collections.
- Public rendering must receive an already filtered, safe context.
- Deleting Owner A must never remove Owner B's data.
- Deletion cleanup must be scoped to the deleting owner's account and Portfolio.
- Direct media URLs for deleted content controlled by Framehold Engine must stop working.

## Dashboard isolation

Framehold Dashboard показывает и изменяет только текущий Portfolio текущего Portfolio Owner. Любой handler, form, queryset и service, работающий в owner-facing контексте, должен получать owner/portfolio boundary явно или выводить его из authenticated user на сервере.

## Public filtering

Публичная выдача не должна опираться на скрытие элементов в шаблоне. Querysets и public context должны быть заранее отфильтрованы по publication state и suspension state.

## Required future permission tests

- Owner A cannot list Owner B's photographs.
- Owner A cannot open Owner B's edit URL.
- Owner A cannot update Owner B's photograph by changing a POSTed object ID.
- Owner A cannot delete Owner B's album.
- Owner A cannot use Owner B's image as a cover.
- Owner A cannot edit Owner B's theme settings.
- Public Visitor cannot see drafts.
- Public Visitor cannot see a suspended portfolio.
- An unverified account cannot upload or create a portfolio.
- A suspended account cannot access owner operations.
- Site Administrator can manage all portfolios.
- Owner A deletion does not affect Owner B.
- Public media URLs controlled by Framehold Engine stop serving deleted assets.
- Deletion retry is safe and does not cross ownership boundaries.
