class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        string = "name : {}\n".format(self.name)
        string += "price : {:.2f}\n".format(self.price)
        string += "description : {}".format(self.description())
        return string


class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"


class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"

    def description(self):
        return "Un po' di Italia nella sua tazza!"


if __name__ == "__main__":
    a = HotBeverage()
    b = Coffee()
    c = Tea()
    d = Chocolate()
    e = Cappuccino()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
