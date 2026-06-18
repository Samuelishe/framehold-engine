from django.contrib.auth import get_user_model


def user_display(user: object) -> str:
    User = get_user_model()
    if isinstance(user, User):
        return user.email
    return ""
