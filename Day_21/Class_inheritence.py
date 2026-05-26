class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eyes = 2
        
                
    def breathe(self):
        print(f"{self.name} is breathing.")
        print(f"{self.name} is a {self.species}.")
    
    
class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type
        
    def breathe(self):
        super().breathe()
        print(f"{self.name} is breathing through gills.")
        
    def swim(self):
        print(f"{self.name} is swimming in {self.water_type} water.")
        

nemo = Fish("Nemo", "Clownfish", "Saltwater")
nemo.breathe()
nemo.swim()