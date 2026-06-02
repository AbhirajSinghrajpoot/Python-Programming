class car:
    
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')
        
my_car = car(make='Toyota', model='Camry', year=2020)
print(my_car.make)   # Output: Toyota