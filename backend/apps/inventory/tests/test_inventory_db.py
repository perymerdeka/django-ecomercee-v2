import pytest
from apps.inventory.models import InventoryModel, CategoryModel

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    """
    Test InventoryCategory DB Fixture
    """
    result = CategoryModel.objects.get(id=id)
    result.name == name
    result.slug == slug
    result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(
    db, category_factory, name, slug, is_active
):
    result = category_factory.create(slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active