# Number of cars
cars = 100
# The sitting capacity of each car
space_in_a_car = 4.0
# Number of availabe drivers
drivers = 30
# Number of passengers that need to be transported
passengers = 90
# Number of cars remainging after all drivers are assigned a vehicle
cars_not_driven = cars - drivers
# Number of cars that have been assigned to a driver
cars_driven = drivers
# Amount of useable seats across all cars assigned to drivers
carpool_capacity = cars_driven * space_in_a_car
# The amount of passengers that one driver can carry depending on how many drivers have been assigned a car.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
