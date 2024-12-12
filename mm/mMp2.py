# mMp2, 10 points
# To implement Propp-Wilson we need a random number generator that returns three random values for a time T. It should store an internal time T, and return the same values if T is ever the same again. Make a struct/class that has methods for this. You can do this by seeding a built-in randomness generator each time, or just save every computed random value in memory and never compute a random value for a time T twice. It should support setting the time T and asking for a new set of random values, which outputs the random value for T and increases T by 1.

from typing import Tuple
import random

class RandomGenerator: # Propp_Wilson
    def __init__(self) -> None:
        self.T = 0
        self.prev_values = dict()

    def get_next(self) -> Tuple[float, float, float]:
        """TODO: add docstring"""
        if self.T not in self.prev_values:
            self.prev_values[self.T] = (random.random(), random.random(), random.random())
        result = self.prev_values[self.T]
        self.T += 1
        return result

    def set_time(self, time: int) -> None:
        """TODO: add docstring"""
        self.T = time


if __name__ == "__main__":
    counter = RandomGenerator()
    counter.set_time(0)
    t1 = counter.get_next()
    print("t1: ", counter.get_next())

    counter.set_time(7)

    counter.set_time(0)
    t2 = counter.get_next()

    print("t2: ", counter.get_next())
    assert t1 == t2  # Consistency test

    counter.set_time(8)
    t3 = counter.get_next()
    assert t1 != t3  # Making sure it changes

    print(counter.get_next())
    print(counter.get_next())


# Þú þarft að búa til gagnagrind/struct/klasa sem vistar teljara T innbyrðis býður upp á eftirfarandi aðgerðir: get_next(): Skilar þrem random tölum x, y, z og hækkar T um einn set_time(t): Setur T sem t. Þetta þarf þá að vera pseudo-random, þannig að x, y, z virðist random en ef ég kalla á til dæmis set_time(0), get_next(), set_time(0), get_next() ætti ég að fá sömu x, y, z bæði skiptin. Það má til dæmis gera þetta með því að vista öll random gildi sem hafa þegar verið búin til í dict. Útskýrir þetta það betur eða er þetta enn óskýrt?