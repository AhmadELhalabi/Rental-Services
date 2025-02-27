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
      