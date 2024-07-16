class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        ab = 0.5 * self.base * self.height
        return ab

    def display(self):
        print('Base: ', self.base)
        print('Height', self.height)
        print('Area',self.calculate_area())


t1 = triangle(10, 20)
t1.display()
