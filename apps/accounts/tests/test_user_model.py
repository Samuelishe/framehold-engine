import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist
from django.db import IntegrityError


@pytest.mark.django_db
def test_configured_user_model_is_accounts_user():
    user_model = get_user_model()

    assert user_model._meta.label == "accounts.User"
    assert user_model.USERNAME_FIELD == "email"
    assert user_model.REQUIRED_FIELDS == []


def test_username_field_does_not_exist():
    user_model = get_user_model()

    with pytest.raises(FieldDoesNotExist):
        user_model._meta.get_field("username")


@pytest.mark.django_db
def test_create_user_normalizes_email_and_defaults_to_non_staff():
    user_model = get_user_model()

    user = user_model.objects.create_user(" Alice@Example.COM ", password="secret")

    assert user.email == "alice@example.com"
    assert not user.is_staff
    assert not user.is_superuser
    assert user.has_usable_password()
    assert user.password != "secret"
    assert str(user) == "alice@example.com"


@pytest.mark.django_db
def test_create_user_rejects_empty_email():
    user_model = get_user_model()

    with pytest.raises(ValueError, match="Email is required"):
        user_model.objects.create_user("  ", password="secret")


@pytest.mark.django_db
def test_mixed_case_equivalents_cannot_become_two_accounts():
    user_model = get_user_model()

    user_model.objects.create_user("Alice@Example.com", password="secret")

    with pytest.raises(IntegrityError):
        user_model.objects.create_user("alice@example.com", password="secret")


@pytest.mark.django_db
def test_create_superuser_enforces_required_flags():
    user_model = get_user_model()

    with pytest.raises(ValueError, match="is_staff=True"):
        user_model.objects.create_superuser(
            "admin@example.test",
            password="secret",
            is_staff=False,
        )

    with pytest.raises(ValueError, match="is_superuser=True"):
        user_model.objects.create_superuser(
            "admin@example.test",
            password="secret",
            is_superuser=False,
        )


@pytest.mark.django_db
def test_create_superuser_uses_email_identity():
    user_model = get_user_model()

    user = user_model.objects.create_superuser("Admin@Example.TEST", password="secret")

    assert user.email == "admin@example.test"
    assert user.is_staff
    assert user.is_superuser
