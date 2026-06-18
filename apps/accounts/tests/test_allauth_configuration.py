from django.conf import settings
from django.urls import resolve


def test_allauth_email_only_foundation_settings():
    assert settings.ACCOUNT_LOGIN_METHODS == {"email"}
    assert settings.ACCOUNT_SIGNUP_FIELDS == ["email*", "password1*", "password2*"]
    assert settings.ACCOUNT_EMAIL_VERIFICATION == "mandatory"
    assert settings.ACCOUNT_USER_MODEL_USERNAME_FIELD is None
    assert settings.ACCOUNT_USER_MODEL_EMAIL_FIELD == "email"
    assert settings.ACCOUNT_UNIQUE_EMAIL is True
    assert settings.ACCOUNT_PREVENT_ENUMERATION is True
    assert settings.ACCOUNT_CONFIRM_EMAIL_ON_GET is False
    assert settings.ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED is False
    assert settings.ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION is False
    assert settings.ACCOUNT_LOGIN_ON_PASSWORD_RESET is False
    assert settings.ACCOUNT_CHANGE_EMAIL is True


def test_allauth_limited_installed_apps_and_middleware():
    assert "allauth" in settings.INSTALLED_APPS
    assert "allauth.account" in settings.INSTALLED_APPS
    assert "allauth.socialaccount" not in settings.INSTALLED_APPS
    assert "allauth.account.middleware.AccountMiddleware" in settings.MIDDLEWARE
    assert "allauth.account.auth_backends.AuthenticationBackend" in settings.AUTHENTICATION_BACKENDS


def test_allauth_account_routes_are_available():
    assert resolve("/accounts/login/").url_name == "account_login"
    assert resolve("/accounts/signup/").url_name == "account_signup"
