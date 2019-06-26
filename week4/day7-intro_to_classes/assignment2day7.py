class TV():
    """
    Docstring >> This is a general class that defines the makeup of a TV station.

    Args:
    brand: string
    on_status: boolean
    current_channel: integer
    life_perc: float
    """
    def __init__(self, brand, on_status, current_channel, life_perc):
        self.brand = brand
        self.on_status = False
        self.current_channel = 0
        self.life_perc = 100.0

    def hit_power(self, on_status):
        """
        Docstring >> this will turn the television on/off, depending on whether it's already on/off (if its on it'll switch it off, and vice versa). We'll add a couple of stipulations with this one:
        Each time the television is turned off, it loses a little bit of life - decrease the life_perc by 0.01 each time the television is turned off.
        Each time the television is turned off the channel should be set to 0.

        Args:

        """
        if self.on_status == True:
            self.on_status == False
            self.current_channel -= 0.01
            self.current_channel = 0
        else:
            on_status = True
            self.current_channel = 3

    def change_channel(self, input_channel):
        """
        Docstring >> this will take in an int to change the channel to a new one.

        Args:
            input_channel: integer
        """
        current_channel = self.current_channel

        if self.on_status == False:
            print("Television is not on!")
        else:
            self.input_channel = self.current_channel

############
Test Data
############
