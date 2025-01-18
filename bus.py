class vehicle:
    def __init__(self,name,max_speed, milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

class bus(vehicle):
    pass

schoolbus=bus("volvo bus",180,12)
print("Vehicle name:",schoolbus.name,"speed:",
schoolbus.max_speed,"mileage:",schoolbus.milage)