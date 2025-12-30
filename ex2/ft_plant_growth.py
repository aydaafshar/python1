# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 11:43:16 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 11:53:11 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name=name
        self.height = height
        self.age = age
    def grow(self,growth):
        self.height +=growth
    def grow_older(self,days):
        self.age += days
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
if __name__ == "__main__":
    rose = Plant("Rose",25,30)
    
    print("=== Day 1 ===")
    print(rose.get_info())

    rose.grow(6)
    rose.grow_older(6)

    print("=== Day 2 ===")
    print(rose.get_info())
    print("Growth this week: +6cm")
    
        