class Vehicle:
    def start_vehicle(self):
        print("Vehicle is starting ......")
    def move(self):
        print("Vehicle can move from one place to another")

class Car(Vehicle):
    wheels=4
    steering=1
    
class BMW(Car):
    top_speed=300
    model_no=3456
    def accelarating(self):
        print("BMW is accelarating..........")

b1=BMW()
b1.start_vehicle()
b1.move()
print(b1.wheels,b1.steering)
b1.accelarating()
print(b1.top_speed,b1.model_no)

c1=Car()
c1.start_vehicle()
print(c1.wheels,c1.steering)
