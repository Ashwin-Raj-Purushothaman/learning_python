#Variables
cars = 120
space_in_a_car = 5.0
drivers = 40
passengers = 100
cars_not_driven = cars - drivers
cars_driven = drivers
car_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars ,"cars available")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", car_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")