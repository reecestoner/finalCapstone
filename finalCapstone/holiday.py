#Defining the destination to start a loop
city_flight = input("Please type one of the following cities: Rome, Milan, Paris or New York:\n").lower()
#Loop will repear whilst the input is not one of the options
while city_flight != "rome" and city_flight != "milan" and city_flight != "paris" and city_flight != "new york":
    city_flight = input("Sorry, we don't provide travel to that destination.\nPlease type one of the following cities: Rome, Milan, Paris or New York:\n").lower()

#Defining the number of nights
num_nights = int(input("Please enter the number of nights you would like to stay:\n"))
#The number of nights has to be valid to exit the loop
while num_nights < 1:
    num_nights = int(input("Please enter at least 1 night.\nHow many nights would your like to stay?\n"))

#Defining the number of days they want to rent a car
rental_days = int(input("How many days of car rental would you like? (0 if no car needed):\n"))
#Must enter a valid number
while rental_days < 0:
     rental_days = int(input(("Please enter at least 0 days.\n")))
 
#Creating a function that multiplies the nights by 45 (cost of the hotel)
def hotel_cost(x,y=45):
    x = num_nights
    return x * y
#Stores the cost of the hotel 
hotel_cost = hotel_cost(num_nights)


#Defining a function that return the flight cost, dependent on the sity
def  plane_cost(x):
    x = city_flight
    if x == "rome":
        return  80
    elif x == "milan":
        return 100
    elif x == "paris":
        return 50
    else:
        return 600
#Stores the plan cost
plane_cost = plane_cost(city_flight)

#Function that multiplies rental days by the daily cost of the car
def car_rental(y, x = 30):
    y = rental_days
    car_cost = x * y
    return car_cost
#stores the car price
car_rental = car_rental(rental_days)
#Only prints the car price if it is not 0
if car_rental != 0:
    print(f"\nYour car will cost £{car_rental}")

#Calculates the total cost of the holiday
def holiday_cost( x, y, z ):
    return x + y + z
holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental) 

#Prints each cost
print(f"The flight cost is £{plane_cost}")
print(f"The cost of the hotel is £{hotel_cost}")
print(f"Therefore, the total cost of your holiday is £{holiday_cost}")

