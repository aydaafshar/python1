# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 14:31:54 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 15:42:53 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def grow(self):
        self.height += 1
        
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = False
    
    def bloom(self):
        self.blooming = True

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

class GardenManager:
    total_gardens_managed = 0 
    
    class GardenStats:
        def __init__(self):
            self.plant_added=0
            self.total_growth=0
            
        def record_plant_added(self):
            self.plant_added += 1
        
        def record_growth(self, amount=1):
            self.total_growth += amount
    
    
    def __init__(self,owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens_managed += 1
        
    def add_plant(self,plant):
        self.plants.append(plant)
        self.stats.record_plant_added()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth(1)
            print(f"{plant.name} grew 1cm")

    def count_types(self):
        regular = 0
        flowering = 0
        prize = 0

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prize += 1
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            else:
                regular += 1

        return regular, flowering, prize
    
    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                if plant.blooming:
                 blooming_text= " (blooming)"
                else:
                 blooming_text = ""
                print(
                    f"- {plant.name}: {plant.height}cm, {plant.color} flowers{blooming_text}, "
                    f"Prize points: {plant.prize_points}"
                )
            elif isinstance(plant, FloweringPlant):
                if plant.blooming:
                 blooming_text= " (blooming)"
                else:
                 blooming_text = ""
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers{blooming_text}")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        
        regular, flowering, prize = self.count_types()
        print()
        print(f"Plants added: {self.stats.plant_added}, Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
    
    @classmethod
    def create_garden_network(cls):
        return cls.total_gardens_managed
    
    @staticmethod
    def validate_height(height):
        return height >= 0
    
    def garden_score(self):
        score=0
        for plant in self.plants:
            score +=plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score
    

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
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
    print(f"Garden scores - Alice: {alice.garden_score()}, Bob: {bob.garden_score()}")
    print("Total gardens managed:", GardenManager.create_garden_network())
        
        
            
        