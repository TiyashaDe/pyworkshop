class vehicles:
    def __init__(self,make,model,fuel="gas"):
        self.make=make
        self.model=model
        self.fuel=fuel
        
class Car(vehicles):
    def __init__(self,make,model,fuel="gas"):
        super().__init__(make,model,fuel)