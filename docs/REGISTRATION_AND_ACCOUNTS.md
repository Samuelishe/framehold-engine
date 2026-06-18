# REGISTRATION_AND_ACCOUNTS

## Статус

Публичная регистрация с обязательным подтверждением email — принятое продуктовое требование Framehold Engine.

Foundation уже содержит custom email-only `accounts.User` и django-allauth configuration. Реальные registration/login/password-reset страницы, email verification UX, onboarding и account lifecycle workflows еще не реализованы.

## Ожидаемый signup flow

1. Visitor открывает страницу регистрации.
2. Visitor вводит email и пароль.
3. Аккаунт создается в состоянии pending email verification.
4. По email отправляется time-limited single-use verification link.
5. До подтверждения email аккаунт не может завершить portfolio onboarding, создать публичное портфолио, загружать фотографии и публиковать контент.
6. После подтверждения пользователь завершает onboarding: выбирает public display name и public portfolio slug; Portfolio создается с safe default theme `minimal_justified`.
7. Пользователь попадает во Framehold Dashboard.

## Правила email и пароля

- Email обязателен.
- Email должен быть уникальным case-insensitively.
- Email должен нормализоваться единообразно.
- Email is the accepted technical login identifier.
- Public username is not required in MVP.
- `Portfolio.slug` is public URL identity.
- `Portfolio.public_name` is display identity.
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

Site Administrator privileges and Portfolio ownership are not mutually exclusive: a User may own a Portfolio and also have Site Administrator permissions.

## Email-only login direction

Accepted direction: email-only login with password. This means email plus password, not passwordless magic-code login.

Why:

- avoids duplicate identity concepts;
- avoids confusion between username and portfolio slug;
- simplifies registration;
- keeps public identity separate from authentication credentials.

Changing email should require verifying the new email address. Old unverified accounts may require scheduled cleanup later. Unverified users cannot create or publish a Portfolio. Registration can be globally disabled. Password reset uses the verified email channel.

## First-publication moderation

Public registration is allowed, and the default publication policy trusts verified Portfolio Owners. Default `publication_approval_policy = none`: verified owner may publish/unpublish/update their own content without manual approval. Optional `first_publication` may be enabled by the operator.

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

Accepted foundation contract:

- application: `apps.accounts`;
- model: `accounts.User`;
- base class: `django.contrib.auth.models.AbstractUser`;
- no `username` field;
- required unique normalized email;
- `USERNAME_FIELD = "email"`;
- `EMAIL_FIELD = "email"`;
- `REQUIRED_FIELDS = []`;
- публичная portfolio identity не зависит от authentication username;
- публичные URL используют `Portfolio.slug`, а не `User.username`.

Custom User manager must support `create_user(email, password=None, **extra_fields)` and `create_superuser(email, password=None, **extra_fields)`, reject empty email, normalize email consistently and preserve Django groups/permissions.

## django-allauth decision

Accepted package: django-allauth regular account package.

Initial constraint direction: `django-allauth>=65.18.0,<66`.

Use only `allauth` and `allauth.account` in foundation. Do not enable `allauth.socialaccount`, social login providers, MFA, headless API, identity-provider functionality, phone authentication, magic-code login, WebAuthn or JWT flows without explicit later decision.

Future settings direction:

```python
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_PREVENT_ENUMERATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_CHANGE_EMAIL = True
```

Signup collects only authentication data. Public name and Portfolio slug are collected during separate onboarding. Do not put Portfolio onboarding fields into django-allauth signup form.

django-allauth rate limits remain enabled; do not set `ACCOUNT_RATE_LIMITS = False`. Initial implementation starts with django-allauth defaults.

## Открытые решения

- Точное представление email verification state.
- Email reuse after deletion.
- Public slug reuse after deletion.
- Exact production cache backend for account rate limits.
- Exact allauth email template/UI styling.

## Запреты

- Не реализовывать custom authentication protocol.
- Не реализовывать custom password hashing.
- Не реализовывать custom session handling.
- Не реализовывать custom token cryptography.
