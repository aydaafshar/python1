# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 12:23:32 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 12:53:49 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
    def __init__(self, name, height=0, age=0):
        self.name=name
        self._height=0
        self._age=0
    
        self.set_height(height)
        self.set_age(age)
    def set_height(self,height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")
    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.age = age
        print(f"age updated: {self._age}cm [OK]")
    def get_height(self):
        return  self._height
    def get_age(self):
        return  self._age
    def get_info(self):
        return f"{self.name} ({self._height}cm, {self._age} days)"

if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")
    
    plant.set_height(25)
    plant.set_age(30)

     
    plant.set_height(-5)
    plant.set_age(-10)

    print(f"Current plant: {plant.get_info()}")

    
    
            
        
        