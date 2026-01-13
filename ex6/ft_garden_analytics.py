class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, cm=1):
        self.height += cm

    def kind(self) -> str:
        return "regular"

    def report_line(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True

    def kind(self) -> str:
        return "flowering"

    def report_line(self):
        if self.blooming:
            blooming_text = " (blooming)"
        else:
            blooming_text = ""

        res = super().report_line()
        return f"{res} , {self.color} flowers{blooming_text}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def kind(self) -> str:
        return "prize"

    def report_line(self):
        res = super().report_line()
        return f"{res}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens_managed = 0

    class GardenStats:
        def __init__(self):
            self.plant_added = 0
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def record_plant_added(self, plant_kind):
            self.plant_added += 1
            if plant_kind == "regular":
                self.regular += 1
            elif plant_kind == "flowering":
                self.flowering += 1
            elif plant_kind == "prize":
                self.prize += 1

        def record_growth(self, amount):
            self.total_growth += amount

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens_managed += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.record_plant_added(plant.kind())
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, cm=1):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.stats.record_growth(cm)
            print(f"{plant.name} grew {cm}cm")

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.report_line())
        print()
        print(
            f"Plants added: {self.stats.plant_added}, "
            f"Total growth: {self.stats.total_growth}cm"
        )
        print(
            f"Plant types: {self.stats.regular} regular, "
            f"{self.stats.flowering} flowering, "
            f"{self.stats.prize} prize flowers"
        )

    def garden_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if plant.kind() == "prize":
                score += plant.prize_points
        return score

    @classmethod
    def create_garden_network(cls):
        return cls.total_gardens_managed

    @staticmethod
    def validate_height(height):
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    print()

    rose.bloom()
    sunflower.bloom()
    print()
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()

    alice.grow_all()
    print()
    alice.report()
    print()

    print("Height validation test:", GardenManager.validate_height(5))
    print(
        f"Garden scores - Alice: {alice.garden_score()},"
        f" Bob: {bob.garden_score()}"
    )
    print("Total gardens managed:", GardenManager.create_garden_network())
