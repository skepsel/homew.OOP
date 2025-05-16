import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_product_creation_and_str():
    p = Product("Мышь", "Обычная", 1000, 10)
    assert str(p) == "Мышь, 1000 руб. Остаток: 10 шт."


def test_product_zero_quantity_raises():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Нулевой", "Ошибка", 100, 0)


def test_product_price_property():
    p = Product("Мышь", "Обычная", 1000, 10)
    assert p.price == 1000
    p.price = 1500
    assert p.price == 1500
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        p.price = -100


def test_product_new_product_method():
    data = {
        "name": "Клавиатура",
        "description": "Игровая",
        "price": 3000,
        "quantity": 5,
    }
    p = Product.new_product(data)
    assert p.name == "Клавиатура"
    assert p.description == "Игровая"
    assert p.price == 3000
    assert p.quantity == 5


def test_creation_logger_mixin(capsys):
    # Создаем продукт и проверяем, что миксин выводит сообщение
    Product("Мышь", "Обычная", 1000, 10)
    captured = capsys.readouterr()
    assert (
        "Product создан с параметрами: ('Мышь', 'Обычная', 1000, 10), {}"
        in captured.out
    )


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


def test_category_average_price():
    c = Category("Разное", "Товары")
    c.add_product(Product("Товар 1", "Описание", 100, 1))
    c.add_product(Product("Товар 2", "Описание", 200, 2))
    assert c.average_price() == 150.0


def test_category_average_price_empty():
    c = Category("Пустая", "Нет товаров")
    assert c.average_price() == 0


def test_category_product_count():
    # Сбрасываем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0
    c = Category("Техника", "Электроника")
    assert Category.category_count == 1
    c.add_product(Product("Наушники", "Беспроводные", 4000, 2))
    assert Category.product_count == 1
