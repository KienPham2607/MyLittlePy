"""
    9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
        Make a 10-sided die and a 20-sided die. Roll each die 10 times.
    """
from random import randint


class Dice:
    seerry = 100

    def __init__(self, side=6):
        self.side = side
        self.name = "NaN"

    def roll_dice(self) -> int:
        return randint(0, self.side)


a_dice = Dice()
print(Dice.seerry)
for _ in range(0, 10):
    print(a_dice.roll_dice())

b_dice = Dice(10)
for _ in range(0, 10):
    print(b_dice.roll_dice())

c_dice = Dice(20)
for _ in range(0, 10):
    print(c_dice.roll_dice())

d_dice = Dice()
