# Import the date class from the datetime module to work with dates
from datetime import date


# Define a class called Person to represent a person with a name, country, and date of birth
class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age

    def display(self):
        print(self.name, self.country, self.calculate_age())


# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person1.display()
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person2.display()
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))
person3.display()
