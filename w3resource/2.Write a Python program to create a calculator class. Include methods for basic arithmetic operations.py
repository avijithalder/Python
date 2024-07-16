class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

    def display(self):
        print(f"Addition: {self.add()}")
        print(f"Subtraction: {self.subtract()}")
        print(f"Multiplication: {self.multiply()}")
        print(f"Division: {self.divide()}")


cal = Calculator(5, 5)
cal.display()
