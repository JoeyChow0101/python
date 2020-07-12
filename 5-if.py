cars = ["bmw", "benz", "audi", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = 'audi'
if car == 'Audi':
    print("True")
else:
    print("False")

age_0 = 11
age_1 = 20
if ((age_0 > 20) and (age_1 > 30)):
    print("True")
elif ((age_0 == 20) and (age_1 == 30)):
    print("Tzerorue")
else:
    print("False")

if ((age_0 > 0) or (age_1 > 30)):
    print("True")
else:
    print("False")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if ('mushrooms' in requested_toppings):
    print("True")

if ('mushroo0ms' not in requested_toppings):
    print("False")

print("====================")


alien_color = 'green'
if alien_color == 'green':
    print("The player got 5 points.")
else:
    print("The player got 10 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("The player got 5 points.")
elif alien_color == 'yellow':
    print("The player got 10 points.")
else:
    print("The player got 15 points.") 

for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("Sorry, we are out of mushrooms right now.")
    else:
        print("Add " + requested_topping + '.')

print("\nFinish making your pizza")

requested_toppings = []

print("====================")

if requested_toppings:
    print("Finish making your pizza.")
else:
    print("Are you sure you want a plain pizza?")

print("====================")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Finish making your pizza~!")
print("====================")