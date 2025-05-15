import pytest
from src.models import Product, Smartphone, LawnGrass, Category


def test_product_creation_and_str():
    p = Product("Мышь", "Обычная", 1000, 10)
    assert str(p) == "Мышь, 1000 руб. Остаток: 10 шт."


def test_smartphone_attributes():
    s = Smartphone("iPhone", "Телефон", 100000, 1, "A16", "14 Pro", 256, "чёрный")
    assert s.efficiency == "A16"
    assert s.model == "14 Pro"
    assert s.memory == 256
    assert s.color == "чёрный"
    assert isinstance(s, Product)


def test_lawngrass_attributes():
    g = LawnGrass("Трава", "Для газона", 300, 5, "Россия", "10 дней", "зелёный")
    assert g.country == "Россия"
    assert g.germination_period == "10 дней"
    assert g.color == "зелёный"
    assert isinstance(g, Product)


def test_add_same_product_type():
    p1 = Product("Клавиатура", "Игровая", 3000, 3)
    p2 = Product("Клавиатура2", "Обычная", 2000, 2)
    total = p1 + p2
    assert total == 3000 * 3 + 2000 * 2


def test_add_different_types_raises():
    s = Smartphone("iPhone", "Телефон", 100000, 1, "A16", "14 Pro", 256, "чёрный")
    g = LawnGrass("Газон", "Для дачи", 500, 10, "Германия", "7 дней", "зелёный")
    with pytest.raises(TypeError):
        _ = s + g


def test_category_add_product_valid():
    c = Category("Техника", "Электроника")
    p = Product("Наушники", "Беспроводные", 4000, 2)
    c.add_product(p)
    assert "Наушники" in c.products


def test_category_add_invalid_type_raises():
    c = Category("Товары", "Разное")
    with pytest.raises(TypeError):
        c.add_product("не продукт")
