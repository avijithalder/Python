class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def x(self):
        print('Move')


class car(vehicle):
    pass


class boat(vehicle):
    def move(self):
        print('sail')


class plane(vehicle):
    def move(self):
        print('fly')


car1 = car("Ford", "Mustang")
car1.x()

boat1 = boat("Ibiza", "Touring 20")
boat1.move()
boat1.x()

plane1 = plane("Boeing", "747")
plane1.move()
plane1.x()

