class Vehical:
# Initializing the vehicle with its type, brand, model, year, rental price, and special attribute (seats or engine capacity)
    def _init_(self, VehicalType, brand, model, year, rental_price_per_day, special_attribute ):
       self.VehicalType = VehicalType
       self.brand = brand 
       self.model = model
       self.year = year
       self.__rental_price_per_day = rental_price_per_day
       self.special_attribute = special_attribute
 
 # Displaying vehicle information based on its type (car or bike)
    def display_info(self):
         if self.VehicalType == "car":
            print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.special_attribute}, Rental Price: ${self.__rental_price_per_day}/day")
         elif self.VehicalType == "bike":
            print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.special_attribute}cc, Rental Price: ${self.__rental_price_per_day}/day")
   
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


vehicles_list = []  # List to store all vehicles
action = None


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
        special_attribute = int(input("Enter seating capacity: "))
    else:
        special_attribute = int(input("Enter engine capacity (cc): "))

    vehicle = Vehical(vehicle_type, brand, model, year, rental_price, special_attribute)
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
  show_vehicle_info(vehicle)
  print()

def show_vehicle_info(vehicle):
    vehicle.display_info()
    