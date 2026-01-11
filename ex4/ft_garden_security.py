class SecurePlant:
    def __init__(self, name, height=0, age=0):
        self.name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_info(self):
        return f"{self.name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm [OK]")
    plant.set_age(30)
    print(f"age updated: {plant.get_age()}days [OK]")

    print()
    plant.set_height(-5)
    plant.set_age(-10)
    print()
    print(f"Current plant: {plant.get_info()}")
