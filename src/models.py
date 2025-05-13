class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0  # количество категорий
    total_products_in_categories = 0  # общее количество продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.total_products_in_categories += len(products)
