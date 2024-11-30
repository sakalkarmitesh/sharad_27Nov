"""
Problem Statement

A vehicle is identified by its mileage (in kms per litre) and fuel left (in litres) in the vehicle. From the fuel left, 5 litres will always be considered as reserve fuel. At any point of time, the driver of the vehicle may want to know:
the maximum distance that can be covered without using the reserve fuel how many kms he/she has already travelled based on the initial fuel the vehicle had
Identify the class name and attributes so as to represent a vehicle from the information given.
     _init()
     Vehicle
     identify_disctance_that_can_be_travelled() mileage fuel left Car
     identify_distance_travelled(initial_fuel)
     Write a Python program to implement the class chosen with its attributes and methods based on the requirements given below:
     identify_distance_that_can_be_travelled(): Return the distance that can be travelled by the vehicle without using the reserve fuel. If the fuel left is less than or equal to reserv fuel, the method should return 0.
     identify_distance_travelled(initial_fuel):
Return the distance so far travelled by the vehicle based on the initial fuel, fuel left and mileage. Assume that initial fuel is always greater than fuel left.
Represent a vehicle and test your program by initializing the instance variables and invoking the appropriate methods."""

class Vehicle:
    def __init__(self, mileage, fuel_left):  # Use __init__ instead of _init_
        self.mileage = mileage
        self.fuel_left = fuel_left

    def identify_distance_that_can_be_travelled(self):
        reserve_fuel = 5
        if self.fuel_left <= reserve_fuel:
            return 0
        else:
            return (self.fuel_left - reserve_fuel) * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        distance_travelled = (initial_fuel - self.fuel_left) * self.mileage
        return distance_travelled

# Represent a vehicle a


# Represent a vehicle and test the program
vehicle = Vehicle(15, 12)  # Mileage: 15 km/l, Fuel Left: 12 liters

# Maximum distance without reserve fuel
distance_without_reserve = vehicle.identify_distance_that_can_be_travelled()
print("Maximum distance without reserve fuel:", distance_without_reserve, "km")

# Distance travelled so far (assuming initial fuel was 18 liters)
initial_fuel = 18
distance_travelled = vehicle.identify_distance_travelled(initial_fuel)
print("Distance travelled so far:", distance_travelled, "km")