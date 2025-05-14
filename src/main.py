from models import Category, Product

if __name__ == "__main__":
    phone = Product("Телефон", "Смартфон", 10000, 5)
    laptop = Product.new_product(
        {"name": "Ноутбук", "description": "Игровой", "price": 150000, "quantity": 3}
    )

    electronics = Category("Электроника", "Разные гаджеты")
    electronics.add_product(phone)
    electronics.add_product(laptop)

    print(electronics)
    print(electronics.products)
    print(phone + laptop)
