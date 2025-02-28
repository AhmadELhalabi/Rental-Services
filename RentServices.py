class Vehical:
# Initializing the vehicle  brand, model, year, rental price
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
 
 # Displaying vehicle information based on its type (car or bike)
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")
   
 # Calculating the rental cost for a given number of days 
    def calculate_rental_cost(self, days):    
        return self.__rental_price_per_day * days

 # Getter for rental price per day
    def get_rental_price(self):
        return self.__rental_price_per_day

 # Setter to update the rental price per day
    def set_rental_price(self, new_price):
        self.__rental_price_per_day = new_price
 
 # Calling the display_info method for polymorphism demonstration
    def show_vehicle_info(vehicle):
      vehicle.display_info()

# Class for Cars
class Car(Vehical):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price()}/day")

# Child class for Bikes
class Bike(Vehical):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price()}/day")


vehicles_list = []  # List to store all vehicles
action = None
previous_action = None

# make the user to enter vehicle details
def create_vehicle():
    while True:
        vehicle_type = input("Enter vehicle type (car/bike): ").strip().lower()
        if vehicle_type in ["car", "bike"]:
            break
        print("Invalid vehicle type! Please enter 'car' or 'bike'.")

    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    year = int(input("Enter vehicle year: "))
    rental_price = float(input("Enter rental price per day: "))

    if vehicle_type == "car":
        seating_capacity = int(input("Enter seating capacity: "))
        vehicle = Car(brand, model, year, rental_price, seating_capacity)

    elif vehicle_type == "bike":
        engine_capacity = int(input("Enter engine capacity (cc): "))
        vehicle = Bike(brand, model, year, rental_price, engine_capacity)

    vehicles_list.append(vehicle)
    print(f"{vehicle_type.capitalize()} added successfully!")

def rent_vehicle():
   
    brand = input("Enter the brand of the vehicle you want to rent: ")
    days = int(input("Enter number of rental days: "))

    for vehicle in vehicles_list:
        if vehicle.brand.lower() == brand.lower() :
            cost = vehicle.calculate_rental_cost(days)
            print(f"Rental cost for {vehicle.brand} {vehicle.model} for {days} days: ${cost}\n")
            return

    print("Vehicle not found.")
    
def update_rental_price():
    
    brand = input("Enter the brand of the vehicle you want to update: ")
    new_price = float(input("Enter new rental price per day: "))

    for vehicle in vehicles_list:
        if vehicle.brand.lower() == brand.lower() :
            vehicle.set_rental_price(new_price)
            print(f"Updated rental price for {vehicle.brand} {vehicle.model}: ${vehicle.get_rental_price()}/day")
            return

    print("Vehicle not found.")

def display_vehicles():
  
 for vehicle in vehicles_list:
  vehicle.display_info()
  print()

#Function to display the menu and get user input.
def menu ():
    
    print("====================================")
    print("Enter 0 to add a vehicle")
    print("Enter 1 to display vehicles")
    print("Enter 2 to rent a vehicle")
    print("Enter 3 to update rental price")
    print("Enter 4 to exit")
    print("====================================")
    return int(input("Choice: "))

# Main loop of the program
while action != 4:  
    action = menu()
    if action in [1, 2, 3] and not vehicles_list:
        print("You must add a vehicle first!")
        print("====================================")
        previous_action = action  
        create_vehicle()  
        action = previous_action  

    if action == 0:
        create_vehicle()
    elif action == 1:
        display_vehicles()
    elif action == 2:
        rent_vehicle()
    elif action == 3:
        update_rental_price()
    elif action == 4:
        print("Program Exit")