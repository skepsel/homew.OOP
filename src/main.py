from models import Category, LawnGrass, Product, Smartphone

if __name__ == "__main__":
    s = Smartphone("iPhone", "Смартфон", 90000, 3, "A15", "13 Pro", 128, "серый")
    g = LawnGrass("Газон", "Для дачи", 500, 10, "Германия", "7 дней", "зеленый")
    p = Product("Наушники", "Bluetooth", 4000, 5)

    tech = Category("Техника", "Электроника и гаджеты")
    tech.add_product(s)
    tech.add_product(p)

    garden = Category("Сад", "Уход за газоном")
    garden.add_product(g)

    print(tech)
    print(tech.products)
    print(garden)
    print(garden.products)
    print(p + p)  # работает
    # print(p + s)  # вызовет TypeError
