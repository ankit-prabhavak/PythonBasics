class Person:

    college = "PSIT"

    def __init__(self, name, birth_year, college):
        self.name = name
        self.birth_year = birth_year
        self.college = college

    def get_info(self):
        print(f"Name: {self.name}, Birth Year: {self.birth_year}, College: {self.college}")

    def calculate_age(self):
        current_year = int(input("Enter the current year: "))
        return current_year - self.birth_year
    
    def is_adult(self):
        age = self.calculate_age()
        if age >= 18:
            print(f"{self.name} is an adult as they are {age} years old.")
        else:
            print(f"{self.name} is not an adult as they are {age} years old.")


# Create an object of the Person class
person1 = Person("John Doe", 2000, "KIT")
person1.get_info()
person1.is_adult()

age = person1.calculate_age()
print(f"{person1.name} is {age} years old.")

print(f"College: {person1.college}")

print(Person.college)

