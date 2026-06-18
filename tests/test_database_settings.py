from django.db import connection


def test_test_database_uses_postgresql_not_sqlite():
    assert connection.vendor == "postgresql"
    assert "sqlite" not in connection.settings_dict["ENGINE"]
