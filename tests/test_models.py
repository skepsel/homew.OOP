import pytest

from src.models import Category, Product


def test_add_product():
    cat = Category("Электроника", "Гаджеты и техника")
    prod = Product("Телефон", "Смартфон", 30000, 10)
    cat.add_product(prod)
    assert "Телефон" in cat.products


def test_product_price_getter_setter():
    p = Product("Ноутбук", "Игровой", 100000, 5)
    assert p.price == 100000
    p.price = 120000
    assert p.price == 120000
    p.price = -500  # Некорректная цена
    assert p.price == 120000  # Цена не изменилась


def test_new_product():
    data = {
        "name": "Мышка",
        "description": "Беспроводная",
        "price": 1500,
        "quantity": 50,
    }
    p = Product.new_product(data)
    assert p.name == "Мышка"
    assert p.price == 1500
    assert p.quantity == 50
