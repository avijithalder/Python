class Students:

    def __init__(self, name, roll, brand, cpu, ram):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop(brand, cpu, ram)

    def show(self):
        print(self.name, self.roll)
        self.lap.Laptopdetails()

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def Laptopdetails(self):
            print(self.brand, self.cpu, self.ram)


s1 = Students("Avijit", 1, 'HP', 'i5', 8)
s2 = Students("Mondira", 2, "Dell", 'i7', 16)
s1.show()
