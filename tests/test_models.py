import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_product_str():
    p = Product("Мышь", "Игровая", 3000, 4)
    assert str(p) == "Мышь, 3000 руб. Остаток: 4 шт."


def test_category_str():
    c = Category("Гаджеты", "Электроника")
    p1 = Product("Телефон", "Смартфон", 10000, 2)
    p2 = Product("Планшет", "iPad", 20000, 3)
    c.add_product(p1)
    c.add_product(p2)
    assert str(c) == "Гаджеты, количество продуктов: 5 шт."


def test_product_add_same_type():
    p1 = Product("Мышь", "Игровая", 3000, 4)
    p2 = Product("Клавиатура", "Механическая", 5000, 2)
    assert p1 + p2 == 3000 * 4 + 5000 * 2


def test_product_add_different_type():
    p = Product("Товар", "Обычный", 1000, 1)
    s = Smartphone("iPhone", "Смартфон", 100000, 1, "A16", "14 Pro", 256, "черный")
    with pytest.raises(TypeError):
        _ = p + s


def test_add_invalid_product_to_category():
    c = Category("Категория", "Описание")
    with pytest.raises(TypeError):
        c.add_product("непродукт")


def test_smartphone_attributes():
    s = Smartphone("iPhone", "Смартфон", 100000, 1, "A16", "14 Pro", 256, "черный")
    assert s.efficiency == "A16"
    assert s.model == "14 Pro"


def test_lawngrass_attributes():
    g = LawnGrass("Газон", "Трава", 500, 5, "Россия", "14 дней", "зелёный")
    assert g.country == "Россия"
    assert g.germination_period == "14 дней"
