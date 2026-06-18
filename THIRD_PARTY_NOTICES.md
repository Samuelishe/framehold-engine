# Third-party notices

Этот файл является человекочитаемым источником учета для намеренно включенных или адаптированных сторонних компонентов и assets в Framehold Engine.

## Текущие включенные компоненты

### Direct runtime Python dependencies

| Component | Version | Purpose | Upstream | License |
| --- | --- | --- | --- | --- |
| Django | 5.2.15 | Core web framework, ORM, migrations, auth/session/security primitives | <https://www.djangoproject.com/> | BSD-3-Clause, verified from installed `django-5.2.15.dist-info/licenses/LICENSE` |
| Wagtail | 7.4.2 | Wagtail Admin, global CMS foundation, standard image/rendition infrastructure | <https://wagtail.org/> | BSD-3-Clause, verified from installed `wagtail-7.4.2.dist-info/licenses/LICENSE` |
| django-allauth | 65.18.0 | Account foundation: email/password login, email verification, password reset direction | <https://allauth.org/> | MIT, verified from installed package metadata |
| django-environ | 0.13.0 | Environment-variable parsing and `DATABASE_URL` support | <https://django-environ.readthedocs.org> | MIT, verified from installed package metadata |
| psycopg | 3.3.4 | PostgreSQL driver | <https://psycopg.org/> | LGPL-3.0-only, verified from installed `psycopg-3.3.4.dist-info/licenses/LICENSE.txt` |
| psycopg-binary | 3.3.4 | Binary Psycopg package selected for initial Windows/Linux development reliability | <https://psycopg.org/> | LGPL-3.0-only, verified from installed `psycopg_binary-3.3.4.dist-info/licenses/LICENSE.txt` |

### Development tools

| Component | Version | Purpose | Upstream | License |
| --- | --- | --- | --- | --- |
| Ruff | 0.15.18 | Formatting and linting | <https://docs.astral.sh/ruff/> | MIT, verified from installed `ruff-0.15.18.dist-info/licenses/LICENSE` |
| pytest | 9.1.0 | Test runner | <https://docs.pytest.org/> | MIT, verified from installed `pytest-9.1.0.dist-info/licenses/LICENSE` |
| pytest-django | 4.12.0 | Django integration for pytest | <https://pytest-django.readthedocs.io/> | BSD-3-Clause, verified from installed package metadata/license text |
| pytest-cov | 7.1.0 | Coverage integration for pytest | <https://pytest-cov.readthedocs.io/> | MIT, verified from installed package metadata |

### Development service images

| Component | Version | Purpose | Upstream | License |
| --- | --- | --- | --- | --- |
| PostgreSQL Docker Official Image | `postgres:18.4-bookworm` | Development PostgreSQL service in `compose.dev.yml` | <https://hub.docker.com/_/postgres>, <https://www.postgresql.org/> | PostgreSQL License for PostgreSQL; Docker image packaging may include additional OS package licenses |

## Transitive dependencies

`uv.lock` records exact direct and transitive Python dependency versions. Transitive dependencies remain under their own licenses. They are not copied into this notice as if they were manually selected Framehold Engine components.

Notable transitive examples include `djangorestframework` and `Pillow`, which are resolved through Wagtail and are not direct Framehold Engine dependencies at this foundation stage.

## Assets

No third-party visual assets, fonts, portfolio screenshots, stock photographs, templates, icons or copied design materials are included in the repository.

Built-in public themes are not implemented yet. Future fonts/icons/assets must be locally bundled or otherwise used only after license verification and attribution review.

## Policy

Third-party components остаются под своими собственными лицензиями. Нельзя удалять upstream copyright или license headers. Нельзя добавлять непроверенную license information. Нельзя перечислять planned dependencies как bundled material до того, как они реально включены.

Каждая future third-party entry должна фиксировать:

- component or asset name;
- author or copyright holder;
- purpose in Framehold Engine;
- upstream project/source URL;
- version, tag, commit or asset identifier where applicable;
- license name;
- SPDX identifier where available;
- license URL or bundled license-file path;
- whether material is unmodified or adapted;
- repository paths containing the material;
- required attribution text;
- additional obligations such as NOTICE preservation.
