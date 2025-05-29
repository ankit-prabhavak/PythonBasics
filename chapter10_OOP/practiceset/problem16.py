# Aggregation

class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.address = address
        self.gender = gender

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state

    def __str__(self):
        return f"{self.city}, {self.pin}, {self.state}"
    

# Example usage
address1 = Address("New York", "10001", "NY")

customer1 = Customer("Jon", "Male", address1)

print(f"Customer Name: {customer1.name}")
print(f"Customer Address: {customer1.address}")
customer1.edit_profile("John Doe", "Los Angeles", "90001", "CA")
print(f"Updated Customer Name: {customer1.name}")
print(f"Updated Customer Address: {customer1.address}")


