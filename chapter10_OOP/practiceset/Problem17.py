# Learning Platform: Python

class User:

    name = None
    email = None
    password = None

    
    def __init__(self):
        self.register()
        self.login()

    def register(self, name=None, email=None, password=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password
        else:
            self.name = input("Enter your name: ")
            self.email = input("Enter your email: ")
            self.password = input("Enter your password: ")

        if not self.name or not self.email or not self.password:
            raise ValueError("All fields are required for registration.")
        

    def login(self, email=None, password=None):
        if not email and not password:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
        if email == self.email and password == self.password:
            print(f"Welcome {self.name}!")
        else:
            print("Invalid email or password. Please try again.")
            return
        

    def logout(self):
        # Logout logic here
        print(f"{self.name} has logged out.")
        self.name = None
        self.email = None
        self.password = None
        

    

class Instructor(User):
    pass

class Student(User):
    pass
