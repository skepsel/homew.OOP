import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_product_str():
    p = Product("Мышь", "Игровая", 3000, 4)
    assert str(p) == "Мышь, 3000 руб. Остаток: 4 шт."


def test_add_same_type():
    p1 = Product("Мышь", "Игровая", 3000, 4)
    p2 = Product("Клавиатура", "Механическая", 5000, 2)
    assert p1 + p2 == 3000 * 4 + 5000 * 2


def test_add_different_type():
    s = Smartphone("iPhone", "Телефон", 100000, 1, "A16", "14 Pro", 256, "черный")
    g = LawnGrass("Газон", "Трава", 500, 10, "Россия", "14 дней", "зелёный")
    with pytest.raises(TypeError):
        _ = s + g


def test_add_invalid_object_to_category():
    c = Category("Техника", "Электроника")
    with pytest.raises(TypeError):
        c.add_product("не продукт")


def test_smartphone_attributes():
    s = Smartphone("Samsung", "Galaxy", 50000, 5, "Exynos", "S22", 128, "белый")
    assert s.model == "S22"
    assert s.memory == 128
    assert s.color == "белый"


def test_lawn_grass_attributes():
    g = LawnGrass("Газон", "Дачный", 200, 20, "Германия", "10 дней", "зеленый")
    assert g.country == "Германия"
    assert g.germination_period == "10 дней"
    assert g.color == "зеленый"
