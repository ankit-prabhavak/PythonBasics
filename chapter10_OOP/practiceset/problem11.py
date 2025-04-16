'''
Problem Statement:
WeCare insurance company wants to calculate the premium of vehicles.
Vehicles are of two types: TwoWheeler and FourWheeler. Each vehicle is identified by a vehicle id, type, cost and premium amount.
For TwoWheeler, the premium is 2% of the cost and for FourWheeler, it is 6% of the cost.
calculate the premium amount and display the vehicle details.'''

class Vehicle:

    def __init__(self, vehicle_id, vehicle_type, cost):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.cost = cost

    def calculate_premium(self):
        if self.vehicle_type == "TwoWheeler":
            return 0.02 * self.cost
        elif self.vehicle_type == "FourWheeler":
            return 0.06 * self.cost
        else:
            raise ValueError("Invalid vehicle type")

    def display_details(self):
        premium = self.calculate_premium()
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Cost: \u20B9{self.cost}")
        print(f"Premium Amount: \u20B9{premium}")


# Example usage
vehicle1 = Vehicle("TW123", "TwoWheeler", 50000)
vehicle1.display_details()

print()

# Example usage for FourWheeler
vechicle2 = Vehicle("FW456", "FourWheeler", 200000)
vechicle2.display_details()

