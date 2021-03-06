from functools import reduce
from objects.food import Food

class Member:
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        '''

        assert isinstance(size, tuple) and len(size) == 3, 'arg: "size" must be a tuple object with len 3'
        assert isinstance(weight, (float, int)), 'arg: "weight" must be a float or int object'

        self.SIZE = size
        self.WEIGHT = weight

class ReproductiveOrgan(Member):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        '''

        super().__init__(size, weight)

        self.MAXIMUM_GENERATION_CAPACITY = round(sum(self.SIZE) * 2)

    def generateDescendants(self) -> tuple:
        pass

class Body(Member):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        '''

        super().__init__(size, weight)

        self.ENERGY_STORAGE_CAPACITY = round(sum(self.SIZE) * 100)
        self.stored_energy = self.ENERGY_STORAGE_CAPACITY / 2

    def supplyEnergy(self, food: Food):

        assert isinstance(food, Food), 'arg: "food" must be a Food object'

        if self.stored_energy + food.stored_energy <= self.ENERGY_STORAGE_CAPACITY:
            self.stored_energy += food.stored_energy

    def spendEnergy(self, energy: float):
        
        assert isinstance(energy, (float, int)), 'arg: "energy" must be a float or int object'

        self.stored_energy -= energy

class Legs(Member):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y: height, z) in meters
        weight -> n in Kg
        '''

        super().__init__(size, weight)

        self.HEIGHT = self.SIZE[1]
        self.MAXIMUM_SPEED = self.HEIGHT