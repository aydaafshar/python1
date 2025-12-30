# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 11:56:13 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 12:07:45 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    print(f"Created: {rose.get_info()}")
    print(f"Created: {oak.get_info()}")
    print(f"Created: {cactus.get_info()}")
    print(f"Created: {sunflower.get_info()}")
    print(f"Created: {fern.get_info()}")
    print()
    print("Total plants created: 5")
        