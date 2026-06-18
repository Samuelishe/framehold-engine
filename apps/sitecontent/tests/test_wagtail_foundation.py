import pytest
from django.contrib.auth import get_user_model
from wagtail.models import Site

from apps.sitecontent.models import HomePage


@pytest.mark.django_db
def test_default_wagtail_site_exists_after_migrations():
    site = Site.objects.get(is_default_site=True)

    assert site.hostname == "localhost"
    assert site.root_page.specific_class is HomePage
    assert site.root_page.title == "Framehold Engine"


@pytest.mark.django_db
def test_homepage_returns_success(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Framehold Engine" in response.content


@pytest.mark.django_db
def test_superuser_can_access_wagtail_admin(client):
    user_model = get_user_model()
    user = user_model.objects.create_superuser("admin@example.test", password="secret")

    client.force_login(user)
    response = client.get("/admin/")

    assert response.status_code == 200
    assert b"Framehold Engine" in response.content


@pytest.mark.django_db
def test_ordinary_user_cannot_access_wagtail_admin(client):
    user_model = get_user_model()
    user = user_model.objects.create_user("owner@example.test", password="secret")

    client.force_login(user)
    response = client.get("/admin/")

    assert response.status_code != 200
