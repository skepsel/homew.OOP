from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class CreationLoggerMixin:
    """Миксин для вывода информации при создании объекта"""

    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"{cls_name} создан с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class Product(CreationLoggerMixin, BaseProduct):
    """Обычный продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Цена должна быть положительной")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )


class Smartphone(Product):
    """Смартфон — наследник Product"""

    def __init__(
            self, name, description, price, quantity, efficiency, model, memory, color
    ):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """Газонная трава — наследник Product"""

    def __init__(
            self, name, description, price, quantity, country, germination_period, color
    ):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


class Category:
    """Категория товаров"""

    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product: Product):
        if not isinstance(product, BaseProduct):
            raise TypeError(
                "Можно добавлять только объекты класса Product и его наследников."
            )
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self):
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return "".join([str(product) + "\n" for product in self.__products])

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
