# assigning a value of 100 to cars.
cars = 100
# assigning float 4.0 to space_in_a_car
space_in_a_car = 4.0
# assigning a value of 30 to drivers.
drivers = 30
# assigning a value of 90 to passengers.
passengers = 90
# assigning a value of variable cars minus drivers to cars_not_driven
cars_not_driven = cars - drivers
# variable cars_driven is assigned a value of variable drivers, making them have the same value.
cars_driven = drivers
# variable carpool_capacity has a value of multiplication between variable cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# variable average_passengers_per_car has a value of passengers divided by a value of cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


'''
Traceback ( most recent c a l l l a s t ) :

F i l e ”ex4 . py” , line 8 , in <module> average_passengers_per_car = car_pool_capacity NameError : name ’ car_pool_capacity ’ i s not defined

The error means that there is no such variable named car_pool_capacity. Instead there is carpool_capacity.
'''

'''
Study drills
1. 4.0 is a float, so if we use a float we will get a float answer in line 14. Otherwise just an index.
2. Ok
3. Ok
4. = is basically an assignment operator. == is when something equals something else.
