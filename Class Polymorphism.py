class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # mathod name same
    def move(self):
        print('Road!')


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # mathod name same
    def move(self):
        print('Water')


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

     # mathod name same

    def move(self):
        print('sky')


car1 = car('Ford', 'mustang')
car1.move()
boat1 = Boat("Ibiza", "Touring")
boat1.move()
plane1 = plane("Boeing", "747")
plane1.move()
