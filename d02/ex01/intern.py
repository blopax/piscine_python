class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == "__main__":
    a = Intern()
    b = Intern("Mark")
    print(a)
    print(b)
    c = b.make_coffee()
    print(c)
    try:
        a.work()
    except Exception as err:
        print(err)
