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
