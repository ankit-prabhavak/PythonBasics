class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__cost = None
        self.__premium_amount = None

    # Getter and Setter methods
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_cost(self, cost):
        self.__cost = cost

    def get_cost(self):
        return self.__cost

    def get_premium_amount(self):
        return self.__premium_amount

    # Method to calculate premium
    def calculate_premium(self):
        if self.__vehicle_type == "TwoWheeler":
            self.__premium_amount = 0.02 * self.__cost
        elif self.__vehicle_type == "FourWheeler":
            self.__premium_amount = 0.06 * self.__cost
        else:
            raise ValueError("Invalid vehicle type")

    # Method to display vehicle details
    def display_vehicle_details(self):
        print(f"Vehicle ID: {self.__vehicle_id}")
        print(f"Vehicle Type: {self.__vehicle_type}")
        print(f"Cost: ₹{self.__cost}")
        print(f"Premium Amount: ₹{self.__premium_amount}")


# Example usage
try:
    vehicle1 = Vehicle()
    vehicle1.set_vehicle_id("TW123")
    vehicle1.set_vehicle_type("TwoWheeler")
    vehicle1.set_cost(50000)
    vehicle1.calculate_premium()
    vehicle1.display_vehicle_details()

    print()

    vehicle2 = Vehicle()
    vehicle2.set_vehicle_id("FW456")
    vehicle2.set_vehicle_type("FourWheeler")
    vehicle2.set_cost(800000)
    vehicle2.calculate_premium()
    vehicle2.display_vehicle_details()

except ValueError as e:
    print(e)