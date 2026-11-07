class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print(self.name,self.model,"drive")

class bike:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print(self.name, self.model,"ride")

class plane:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print(self.name, self.model,"fly")
class boat:
    def __init__(self,name, model):
        self.name = name
        self.model = model

    def move(self):
        print(self.name, self.model,"sail")

car1 = car("Mercedes", "Benz")
bike1 = bike("Honda","CG125")
plane1 = plane("Airbus", "A380-800")
boat1 = boat("Yacht", "Oceanic")

for x in(car1, bike1, plane1, boat1):
    x.move()