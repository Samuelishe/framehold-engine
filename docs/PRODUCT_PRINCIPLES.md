# PRODUCT_PRINCIPLES

Этот документ фиксирует принципы, по которым принимаются продуктовые и архитектурные решения Framehold Engine. Это не список функций и не замена `PRODUCT_VISION.md`.

## 1. Trust by default

Verified Portfolio Owner доверяется по умолчанию.

Обычная публикация не требует ручного Site Administrator approval, если operator явно не включает moderation policy. Site Administrator suspension и emergency controls остаются доступными.

## 2. Published means accessible

Published photographs намеренно viewable и saveable.

Продукт не должен притворяться, что browser-visible images нельзя скопировать.

## 3. No fake DRM

Нельзя отключать context menus, добавлять transparent blocking overlays, использовать canvas-only image hiding, obscure URLs как fake security mechanism или добавлять DRM.

## 4. Private means actually protected

Draft, unpublished, suspended, deleted и private source media должны защищаться server-side rules и storage boundaries.

Absence of a link is not access control.

## 5. Users control their content and data

Portfolio Owners контролируют публикацию своего контента и могут инициировать Delete account and all data.

User-uploaded photographs остаются user content и не становятся AGPL-licensed автоматически.

## 6. No social-network pressure

В MVP нет likes, follows, ratings, visitor comments, direct messages, activity feeds или engagement mechanics.

## 7. Simple defaults, explicit advanced controls

Default user path должен быть простым.

Moderation, stricter discoverability, raw-source exposure, external analytics и другие advanced controls должны быть deliberate operator или owner choices.

## 8. Proportional security, not security theatre

Использовать real server-side protection, email verification, rate limiting, safe uploads и ownership isolation.

Не вводить SMS, identity documents, mandatory 2FA, CAPTCHA systems или enterprise identity complexity без demonstrated need.

## 9. No dark patterns or artificial lock-in

Нельзя намеренно усложнять export, saving, unpublishing или deletion контента.

Нельзя использовать manipulative retention или engagement patterns.

## 10. No mandatory telemetry or phone-home behavior

Обычная Framehold Engine installation не должна требовать связи с project-operated infrastructure.

Нет mandatory analytics, telemetry, tracking, update beacon или external service dependency.

## 11. Operator controls the instance; Portfolio Owner controls the portfolio

Operator контролирует global instance policy, security, registration и suspension.

Portfolio Owner контролирует portfolio content и presentation в рамках этих global limits.

## 12. Portfolio engine, not universal photo cloud

Framehold Engine не предназначен быть:

- photo backup system;
- RAW developer;
- Digital Asset Management system;
- Lightroom replacement;
- generic file cloud;
- social network.
