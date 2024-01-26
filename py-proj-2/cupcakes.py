
from abc import ABC, abstractmethod
import csv

# classes for creating cupcakes
class Regular_cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
    
class Mini_cupcake(Regular_cupcake):
    size = "mini"

    def calculate_price(self, quantity):
        return quantity * self.price

class Large_cupcake(Regular_cupcake):
    size = "large"

    def calculate_price(self, quantity):
        return quantity * self.price

# Adds a cupcake
def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            "size": cupcake.get("size", ""),
            "name": cupcake.get("name", ""),
            "price": cupcake.get("price", ""),
            "flavor": cupcake.get("flavor", ""),
            "frosting": cupcake.get("frosting", ""),
            "sprinkles": cupcake.get("sprinkles", ""),
            "filling": cupcake.get("filling", "")
        })

# finds a cupcake with the corresponding name and returs all its attributes
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None   


def get_cupcakes(file):
    cupcakes_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Create a dictionary for each cupcake
            cupcake_dict = {
                'size': row[0],
                'name': row[1],
                'price': row[2],
                'flavor': row[3],
                'frosting': row[4],
                'sprinkles': row[5],
                'filling': row[6],
            }
            
            cupcakes_list.append(cupcake_dict)
    return cupcakes_list



