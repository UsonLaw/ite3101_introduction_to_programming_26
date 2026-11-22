class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        print(self.name)
        print(self.age)


hippo = Animal("Anderson", 36)
sloth = Animal("Dale", 15)
ocelot = Animal("Fuzzy", 7)

print(hippo.health)
print(sloth.health)
print(ocelot.health)