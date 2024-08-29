class Student:
    school = "Avijit Coding School"

    # Instanse Method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class Method
    @classmethod
    def getschoolname(cls):
        print(cls.school)

    # static Method
    @staticmethod
    def info():
        print("This is Static Method")


s1 = Student(10, 20, 30)
s2 = Student(10, 30, 45)

print(s1.avg())
s1.getschoolname()
Student.getschoolname()
s1.info()
Student.info()
