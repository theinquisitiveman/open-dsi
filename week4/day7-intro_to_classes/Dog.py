class Dog():
    def __init__(self, size, color, name):
        self.size = size
        self.color = color
        self.name = name
        self.happiness = 5

    def eat(self):
        self.happiness += 3
        print(self.happiness)

    def walk(self):
        self.happiness +=4
        print(self.happiness)

    def bark(self):
        self.happiness -= 2
        print(self.happiness)

    def __str__(self):
        return self.name + ' has happness ' + str(self.happiness)

    def __len__(self):
        return
