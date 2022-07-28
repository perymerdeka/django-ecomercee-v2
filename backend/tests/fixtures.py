import pytest

@pytest.fixture
def create_admin_user(django_user_model):
    user = django_user_model.objects.create_superuser(
        username="dev",
        email="dev@dev.id",
        password="dev"
    )
    return user