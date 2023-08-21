class Car:
    runs=True
    
    def start(self):
        if self.runs:
            print("Car is started.Vroom vroom!")
        else:
            print("Car is broken:(")
 my_car =Car()
 my_car.runs=False
 print(f"My car runs:{my_car.runs}")  
 my_car.start() 
 my_other_car=Car()   
 my_other_car.start() 
type(42)
type("hi") 
isinstance("hi",int)
isinstance("hi",str)
print(isinstance(my_other_car,Car))

class Car:
    runs=True
    
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        if self.runs:
            print(f"your{self.make} {self.model} is started.Vroom vroom!")
        else:
            print(f"your{self.make} {self.model} is broken:(")
my_car=Car("Ford","Thunderbird")
my_car.start()