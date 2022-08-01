import pytest
from django.core.management import call_command

@pytest.fixture
def create_admin_user(django_user_model):
    user = django_user_model.objects.create_superuser(
        username="dev",
        email="dev@dev.id",
        password="dev"
    )
    return user

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    """
    print("Loading DB fixtures")
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")