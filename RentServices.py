class Vehical:
# Initializing the vehicle with its type, brand, model, year, rental price, and special attribute (seats or engine capacity)
    def _init_(self, VehicalType, brand, model, year, RentPricePerDay, SpecialAttribute ):
       self.VehicalType = VehicalType
       self.brand = brand 
       self.model = model
       self.year = year
       self.RentPricePerDay = RentPricePerDay 
       self.SpecialAttribute = SpecialAttribute
 
 # Displaying vehicle information based on its type (car or bike)
    def displayinfo(self):
         if self.VehicalType == "car":
            print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.SpecialAttribute}, Rental Price: ${self.RentPricePerDay}/day")
         elif self.VehicalType == "bike":
            print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.SpecialAttribute}cc, Rental Price: ${self.RentPricePerDay}/day")