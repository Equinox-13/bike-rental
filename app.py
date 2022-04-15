# Bike Rental System

import datetime
from datetime import timedelta

class BikeRental:
    def __init__(self, stock=0):
        """
        Constructor that instantiates bike rental shop
        """
        self.stock = stock
    
    def display(self):
        """
        Display the bikes currently available for rent in the shop
        """
        print(f"We have currently {self.stock} bikes available to rent.")
        return self.stock
    
    def validate_input(self,no_of_bike):
        """
        Validate input
        """
        if no_of_bike <= 0:
            print("No. of Bikes should be positive.")
            return None
        else:
            return True
    
    def check_stock_level(self, no_of_bike):
        """
        Do not rent if the stock is less than requested
        """
        if no_of_bike > self.stock:
            print(f"Sorry! We have currently {self.stock} bike available to rent.")
            return None
        else:
            return True
            
    def rent_bike_on_hourly_basis(self, no_of_bike):
        """
        Rent bike on hourly basis
        """
        input_check = self.validate_input(no_of_bike)
        stock_check = self.check_stock_level(no_of_bike)
        if input_check and stock_check:
            now = datetime.datetime.now()
            print("==============================")
            print(f"You have rented {no_of_bike} bike on hourly basis today at {now.hour}")
            print("You will be charged $5 for each hour per bike.")
            print("==============================")
            print("We hope that you enjoy our service.")
            self.stock = self.stock - no_of_bike
            return now
    
    def rent_bike_on_daily_basis(self, no_of_bike):
        """
        Rent bike on daily basis
        """
        input_check = self.validate_input(no_of_bike)
        stock_check = self.check_stock_level(no_of_bike)
        if input_check and stock_check:
            now = datetime.datetime.now()
            print(f"You have rented {no_of_bike} bike on daily basis today at {now.hour}")
            print("You will be charged $20 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock = self.stock - no_of_bike
            return now
            
    def rent_bike_on_weekly_basis(self, no_of_bike):
        """
        Rent bike on weekly basis
        """
        input_check = self.validate_input(no_of_bike)
        stock_check = self.check_stock_level(no_of_bike)
        if input_check and stock_check:
            now = datetime.datetime.now()
            print(f"You have rented {no_of_bike} bike on weekly basis today at {now.hour}")
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock = self.stock - no_of_bike
            return now
    
    def select_rental_plan(self, no_of_bike, rental_basis):
        """
        Select the rental plan based on the rental_basis parameter
        """
        if rental_basis == 1:
            self.rent_bike_on_hourly_basis(no_of_bike)
        elif rental_basis == 2:
            self.rent_bike_on_daily_bais(no_of_bike)
        elif rental_basis == 3:
            self.rent_bike_on_weekly_basis(no_of_bike)
    
    def return_bill(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        
        # Extract the tuple and initiate the bill
        rental_time, rental_basis, no_of_bike = request
        bill = 0
        
        # Issue a bill only if all three parameters are not null
        if rental_time and  rental_basis and no_of_bike:
            self.stock = self.stock + no_of_bike
            now = datetime.datetime.now()
            rental_period = now - rental_time 
            
            # Hourly bill calculation
            if rental_basis == 1:
                bill = rental_period.seconds / 3600 * 5 * no_of_bike
            
            # Daily bill calculation
            elif rental_basis == 2:
                bill = rental_period.days * 20 * no_of_bike
            
            # Weekly bill calculation
            elif rental_basis == 3:
                bill = rental_period.days / 7 * 60 * no_of_bike
            
            # Family discount calculation
            if 3 <= no_of_bike <= 5:
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            print("##############################")
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print(f"The total amount that needs to be paid is {round(bill)}$")
        else:
            print("Are you sure you rented a bike with us?")
            return None
            

class Customer:
    def __init__(self):
        """
        Constructor method that instantiates customer object
        """
        self.bike = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0
    
    def rental_plan_menu(self):
        """
        Display the rental plan menu and validate the input
        return: rental_basis
        """
        print("======Rental Plans==============")
        print("1. Hourly Basis")
        print("2. Daily Basis ")
        print("3. Weekly Basis")
        rental_basis = input("Which rental plan would you like to opt for? ")
        try:
            rental_basis = int(rental_basis)
        except ValueError:
            print("Please select a no. from 1, 2 or 3!")
            return -1
        if rental_basis <= 0:
            print("Please select a positive no.")
            return -1
        else:
            return rental_basis
    
    def validate_no_of_bikes(self, bikes):
        """
        Validate input for no. of bikes
        return: bikes
        """
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        else:
            return bikes
    
    def calculate_rental_time(self):
        """
        Calculate rental time
        return: rental_time
        """
        rental_time = int(input("Rented duration in Hrs?: "))
        rental_time = datetime.datetime.now() + timedelta(hours=-rental_time)
        return rental_time
    
    def request_bike(self):
        """
        Takes a request from the customer for the no. of bikes and rental basis
        """
        bikes = input("How many bikes would you like to rent? ")
        self.bikes = self.validate_no_of_bikes(bikes)
        self.rental_basis = self.rental_plan_menu()
        
        return self.bikes, self.rental_basis
    
    def return_bike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        bikes = input("How many bikes would you like to return? ")
        self.bike = self.validate_no_of_bikes(bikes)
        self.rental_time = self.calculate_rental_time()
        self.rental_basis = self.rental_plan_menu()
        
        if self.rental_time and self.rental_basis and self.bike:
            return self.rental_time, self.rental_basis, self.bike
        else:
            return 0,0,0
    
    
shop = BikeRental(50)
shop.display()

customer1 = Customer()

# Rent a bike
no_of_bike, rental_basis = customer1.request_bike()
shop.select_rental_plan(no_of_bike, rental_basis)

# Return a bike
request = customer1.return_bike()
shop.return_bill(request)
