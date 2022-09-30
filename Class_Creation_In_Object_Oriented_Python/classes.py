# Define static class
class CarStatic:
    make = "buick"
    model = "lesabre"
    color = "red"
    year = 2013
    price = 10000


car_static = CarStatic()
print("Model: " + car_static.model)


# Define Constructor
class CarConstructor:
    def __init__(self, make="unknown", model="unknown", color="unknown", year=-1, price=-1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self._price = price

    # Define the property, this is the getter
    @property
    def price(self):
        return self._price

    # Define the setter, this is used to set the value
    @price.setter
    def price(self, p):
        if p <= 0:
            raise ValueError("Price is zero or less!")
        print("Setter for price called. Price set to ", p)
        self._price = p

    # Override method for printing as a string
    # __str__ method by default returns the name of the class and location of the object
    def __str__(self):
        return "Car: Make = " + str(self.make) + ", Model = " + str(self.model) +\
                ", Color = " + str(self.color) + ", Year = " + str(self.year) + \
               ", Price = " + str(self.price)


car_constructor = CarConstructor()
print("Model: " + car_constructor.model)

car = CarConstructor("buick", "lesabre", "red", 2013, 10000)

print("Model: " + car.model)

# Setting the price. car.price = -1 would cause a value error
car.price = 1000

# Print the new class string method, which now provides much more useful information
print(car)


# Read data from a file.
# Use FH as a file handle, with argument r for read only
fh = open("cars.csv", "r")
# Then get the data from each line, this created a list
cars_data = fh.readlines()
# Remove column names, this is the first entry in the list
cars_data.pop(0)

cars_list = []

for rawstring in cars_data:
    make, model, color, year, price = rawstring.split(",")
    cars_list.append(CarConstructor(make, model, color, int(year), float(price)))

cars_list.sort(key=lambda cars: cars.price)

print("\nAll cars:")
print(*cars_list, sep="\n")
