class Cat():
    """
    This docstring will discuss how to interact with our Cat class.

    Parameters:
        name: str
        laziness_level: int
           This holds how lazy the cat is on a scale of 1 to 10.
       location: str
           This holds where the cat is currently located at.
    """

    def __init__(self, name, laziness_level, location):
        self.name = name
        self.laziness_level = 5
        self.location = "home"

    def sense_earthquake(self, earthquake):
       """Checks if the cat senses an earthquake, and if so changes the cat's
       location to 'gone dark'.

       Args:
           earthquake: boolean
               Holds a True or False as to whether there was an earthquake.
       """
       if earthquake == True:
           self.location = "gone dark"
           return self.name + " has gone dark!"
       else:
           return self.location

class Car():
    """
    Docstring >> This class defines a car.

    Args:
        model: string
        color: string
        tank_size: integer
    """

    def __init__(self, model, color, tank_size):
        self.model = model
        self.color = "red"
        self.tank_size = 20
        self.gallons_of_gas = self.tank_size # We're assuming its tank is full.

    def drive(self, miles_driven):
        """
        Docstring >> This method will be used to steer the car to drive.

        Args:
            miles_driven: integer
            gallons_of_gas: integer
        """
        self.miles_driven = miles_driven
        self.gallons_of_gas -= miles_driven / 10

class Plane():
    """
    Docstring >> This class defines the general framework for a plane.

    Args:
        destination: string
        departure_city: string
        trip_distance: integer
    """

    def __init__(self, destination, departure_city, trip_distance):
        self.destination = destination
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self):
        destination = self.departure_city, self.destination = self.destination, self.departure_city
        print(destination)
