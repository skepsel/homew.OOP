from src.models import Category, Product


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 29999.99, 5)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 29999.99
    assert product.quantity == 5


def test_category_initialization():
    Category.category_count = 0
    Category.total_products_in_categories = 0

    product1 = Product("Телефон", "Смартфон", 29999.99, 5)
    product2 = Product("Наушники", "Беспроводные", 4999.50, 15)
    category = Category("Электроника", "Гаджеты", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Гаджеты"
    assert category.products == [product1, product2]
    assert Category.category_count == 1
    assert Category.total_products_in_categories == 2


def test_multiple_categories_and_products():
    Category.category_count = 0
    Category.total_products_in_categories = 0

    p1 = Product("Телевизор", "Smart TV", 49999.0, 2)
    p2 = Product("Микроволновка", "Для кухни", 8999.0, 3)
    c1 = Category("Бытовая техника", "Описание", [p1, p2])

    p3 = Product("Мышка", "Компьютерная", 999.0, 10)
    c2 = Category("Периферия", "Комплектующие", [p3])

    assert Category.category_count == 2
    assert Category.total_products_in_categories == 3
