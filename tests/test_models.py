import pytest
from src.models import Product, Category


def test_product_str():
    product = Product("Телефон", "Смартфон", 10000, 5)
    assert str(product) == "Телефон, 10000 руб. Остаток: 5 шт."


def test_category_str():
    category = Category("Электроника", "Гаджеты")
    product1 = Product("Телефон", "Смартфон", 10000, 5)
    product2 = Product("Планшет", "iPad", 20000, 2)
    category.add_product(product1)
    category.add_product(product2)
    assert str(category) == "Электроника, количество продуктов: 7 шт."


def test_product_add():
    p1 = Product("Ноутбук", "MacBook", 150000, 1)
    p2 = Product("Монитор", "LG", 20000, 2)
    assert p1 + p2 == 150000 * 1 + 20000 * 2


def test_price_setter_valid():
    p = Product("Мышь", "Игровая", 3000, 5)
    p.price = 5000
    assert p.price == 5000


def test_price_setter_invalid(capsys):
    p = Product("Клавиатура", "Механическая", 4000, 4)
    p.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 4000
