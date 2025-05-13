class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict):
        """Создаёт новый продукт из словаря."""
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )

    @property
    def price(self):
        """Геттер цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер с проверкой."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


from typing import List


class Category:
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products: List[Product] = []

    def add_product(self, product):
        """Добавляет продукт в приватный список и увеличивает счётчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми продуктами."""
        return "".join(
            [
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
                for product in self.__products
            ]
        )
