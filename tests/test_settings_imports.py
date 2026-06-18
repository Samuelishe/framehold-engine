import os
import subprocess
import sys

from django.conf import settings


def test_auth_user_model_setting():
    assert settings.AUTH_USER_MODEL == "accounts.User"


def test_dev_and_test_settings_import():
    subprocess.run(
        [sys.executable, "-c", "import framehold.settings.dev; import framehold.settings.test"],
        check=True,
    )


def test_prod_settings_fail_without_required_secret():
    env = os.environ.copy()
    for key in (
        "DJANGO_SECRET_KEY",
        "DJANGO_ALLOWED_HOSTS",
        "FRAMEHOLD_PUBLIC_ORIGIN",
        "DATABASE_URL",
    ):
        env.pop(key, None)
    env["DJANGO_SETTINGS_MODULE"] = "framehold.settings.prod"

    result = subprocess.run(
        [sys.executable, "-c", "import framehold.settings.prod"],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "DJANGO_SECRET_KEY" in result.stderr
