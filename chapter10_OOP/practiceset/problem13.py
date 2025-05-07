class Customer:
    # Class-level list to store all instances
    all_customers = []

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        # Add the instance to the class-level list
        Customer.all_customers.append(self)

    def greet(self):
        if self.gender == 'Male':
            print(f"Hello Mr. {self.name}")
        else:
            print(f"Hello Ms. {self.name}")


# Create instances
customer1 = Customer("John", "Male")
customer2 = Customer("Ananya", "Female")

# Iterate over all instances
for customer in Customer.all_customers:
    customer.greet()