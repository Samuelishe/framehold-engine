# REGISTRATION_AND_ACCOUNTS

## Статус

Публичная регистрация с обязательным подтверждением email — принятое продуктовое требование Framehold Engine. Реализации пока нет.

## Ожидаемый signup flow

1. Visitor открывает страницу регистрации.
2. Visitor вводит email и пароль.
3. Аккаунт создается в состоянии pending email verification.
4. По email отправляется time-limited single-use verification link.
5. До подтверждения email аккаунт не может завершить portfolio onboarding, создать публичное портфолио, загружать фотографии и публиковать контент.
6. После подтверждения пользователь завершает onboarding: выбирает public display name, public portfolio slug, initial theme и создает первое Portfolio.
7. Пользователь попадает во Framehold Dashboard.

## Правила email и пароля

- Email обязателен.
- Email должен быть уникальным case-insensitively.
- Email должен нормализоваться единообразно.
- Password hashing выполняет только Django.
- Password validation использует установленные механизмы Django.
- Password reset использует verified email channel.
- Account-sensitive формы не должны без необходимости раскрывать, существует ли email.

## Verification rules

- Verification tokens не должны использовать custom cryptography.
- Verification links должны истекать.
- Verification links должны быть single-use.
- Resend verification должен иметь cooldown.
- Signup, login, verification resend и password reset должны быть rate-limited.
- Exact rate limits и token expiration values пока не зафиксированы.

## Account states

Планируемые состояния:

- pending email verification;
- verified active;
- suspended;
- deletion processing;
- deleted;
- possibly disabled/deactivated.

Self-registered users являются regular non-staff users. Регистрация никогда не должна автоматически давать `is_staff`, `is_superuser`, Wagtail Admin access, глобальный доступ к Wagtail collections или page tree permissions.

## Administrative controls

Site Administrator должен иметь возможность:

- отключить новые регистрации глобально;
- suspend/reactivate account;
- inspect/manage portfolios при необходимости;
- выполнять emergency corrective actions.

## Account deletion entry point

Verified Portfolio Owner должен иметь self-service action **Delete account and all data** в Framehold Dashboard settings.

Требования:

- re-authentication или sufficiently recent authenticated session;
- explicit irreversible confirmation;
- immediate public removal of Portfolio;
- session/token revocation;
- login, upload and editing blocked after confirmation;
- deletion of owned active application data and controlled media assets.

Suspension and deletion are different. Suspension is reversible. Deletion is irreversible after confirmation boundary.

## Ограничение email verification

Email verification подтверждает контроль над почтовым ящиком и не дает повторно зарегистрироваться с тем же unique email. Это не доказывает, что один физический человек владеет только одним аккаунтом, и не предотвращает намеренную регистрацию с несколькими email-адресами.

MVP security должен оставаться пропорциональным.

## Не требуется для MVP

- CAPTCHA;
- Cloudflare Turnstile;
- phone verification;
- SMS;
- authenticator applications;
- mandatory two-factor authentication;
- social login;
- identity documents;
- enterprise identity providers.

Эти меры можно пересмотреть только при реальном abuse.

## Custom User model decision

Принятое архитектурное решение: Framehold Engine должен использовать custom Django user model с самого начала, до первых application migrations.

Текущее направление:

- application area: `accounts`;
- custom User на базе `AbstractUser` или другой стандартной Django base;
- обязательный уникальный email;
- публичная portfolio identity не зависит от authentication username;
- публичные URL используют `Portfolio.slug`, а не `User.username`.

## Открытые решения

- Login будет email-only или email plus internal username.
- Какая mature authentication package реализует registration и verification.
- Будет ли выбран `django-allauth` или другое established solution.
- Точное представление email verification state.
- Email reuse after deletion.
- Public slug reuse after deletion.

## Запреты

- Не реализовывать custom authentication protocol.
- Не реализовывать custom password hashing.
- Не реализовывать custom session handling.
- Не реализовывать custom token cryptography.
