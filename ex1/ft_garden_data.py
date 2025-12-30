# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 11:20:55 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 11:35:05 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self,name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    rose=Plant("Rose",25,30)
    sunflower=Plant("Sunflower",80,45)
    cactus=Plant("Cactus",15,120)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


