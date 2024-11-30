"""
WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types - "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers. Calculate the premium amount and display the vehicle details.
Identify the class name and attributes to represent vehicles. Drag and drop the chosen class name, attributes and methods into the appropriate section of the box shown below.
"""
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost):  # Use __init__ instead of _init_
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.vehicle_cost = vehicle_cost
        self.premium_amount = self.calculate_premium()

    def calculate_premium(self):
        if self.vehicle_type == "Two Wheeler":
            return self.vehicle_cost * 0.02
        elif self.vehicle_type == "Four Wheeler":
            return self.vehicle_cost * 0.06
        else:
            raise ValueError("Invalid vehicle type")

    def display_vehicle_details(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Vehicle Cost: {self.vehicle_cost}")
        print(f"Premium Amount: {self.premium_amount}")

# Example usage:
vehicle1 = Vehicle("V123", "Two Wheeler", 50000)
vehicle2 = Vehicle("V456", "Four Wheeler", 100000)

vehicle1.display_vehicle_details()
vehicle2.display_vehicle_details()