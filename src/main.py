from src.models import Category, Product


def main():
    # Создаем продукты
    product1 = Product("Телефон", "Смартфон с экраном 6.5 дюйма", 29990.99, 10)
    product2 = Product("Ноутбук", "Ультрабук 14 дюймов", 79990.50, 5)
    product3 = Product("Часы", "Умные часы с пульсометром", 12990.00, 20)

    # Создаем категории
    category1 = Category(
        "Электроника", "Категория электронных товаров", [product1, product2]
    )
    category2 = Category("Гаджеты", "Носимые устройства", [product3])

    # Выводим информацию
    print(f"Категорий создано: {Category.category_count}")
    print(f"Товаров создано: {Category.product_count}")

    print("\nИнформация о категориях:")
    for category in [category1, category2]:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print("Товары:")
        for product in category.products:
            print(f" - {product.name}: {product.price} руб. ({product.quantity} шт.)")


if __name__ == "__main__":
    main()
