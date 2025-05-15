from models import Category, LawnGrass, Product, Smartphone

if __name__ == "__main__":
    p = Product("Наушники", "Bluetooth", 4000, 5)
    s = Smartphone("iPhone", "Телефон", 90000, 3, "A15", "13 Pro", 128, "серый")
    g = LawnGrass("Газон", "Для дачи", 500, 10, "Германия", "7 дней", "зеленый")

    tech = Category("Техника", "Электроника и гаджеты")
    garden = Category("Сад", "Газоны и растения")

    tech.add_product(p)
    tech.add_product(s)
    garden.add_product(g)

    print(tech)
    print(tech.products)

    print(garden)
    print(garden.products)