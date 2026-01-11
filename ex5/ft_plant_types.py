class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def basic_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        base = super().basic_info()
        return f"{base}, {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_info(self):
        base = super().basic_info()
        return f"{base}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        base = super().basic_info()
        return f"{base}, {self.harvest_season} harvest"

    def nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print()
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1500, 35)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "autumn", "beta-carotene")

    print(f"🌹{rose.get_info()}")
    rose.bloom()
    print()
    print(f"🌷{tulip.get_info()}")
    tulip.bloom()
    print()

    print(f"🎄{oak.get_info()}")
    oak.produce_shade()
    print()

    print(f"🌳{pine.get_info()}")
    pine.produce_shade()
    print()

    print(f"🍅{tomato.get_info()}")
    tomato.nutrition()
    print()

    print(f"🥕{carrot.get_info()}")
    carrot.nutrition()
