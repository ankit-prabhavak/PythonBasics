class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

        def display_info(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Address: {self.address}")
            

   
class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def change_address(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

Address1 = Address("123 Main St", "Springfield", "IL", "62701")
Customer1 = Customer("John Doe", 30, Address1)

Customer1.display_info()