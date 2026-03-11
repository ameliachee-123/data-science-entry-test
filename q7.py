class Car:
    """
    This class represents a car.
    It stores the make, model, and year of the car.
    """

    def __init__(self, make, model, year):
        # Initialize the attributes when a new car object is created
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # Print the car information in the format "Year Make Model"
        print(f"{self.year} {self.make} {self.model}")


# Create a car object using the given details
car1 = Car("Toyota", "Corolla", 2020)

# Call the method to display the car description
car1.describe_car()
