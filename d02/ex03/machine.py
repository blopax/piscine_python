import random

import beverages


def randomize(int_max):
    return random.randint(0, int_max)


class CoffeeMachine:
    def __init__(self):
        self.served_bev = 0

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.served_bev = 0

    def serve(self, cls):
        rand = randomize(1)
        self.served_bev += 1
        try:
            if self.served_bev > 10:
                raise (self.BrokenMachineException())
            elif rand == 0:
                return cls()
            else:
                return self.EmptyCup()
        except Exception as err:
            print(err)


if __name__ == "__main__":
    machine = CoffeeMachine()
    drink = [beverages.Cappuccino, beverages.Tea, beverages.Coffee, beverages.Chocolate]
    for serve in range(22):
        beverage_choice = drink[randomize(3)]
        beverage_served = machine.serve(beverage_choice)
        if isinstance(beverage_served, beverages.HotBeverage):
            print(beverage_served.name)
        else:
            machine.repair()
