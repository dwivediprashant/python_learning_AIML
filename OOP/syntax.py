# class : blueprint for objects thatd efines what data/properties should an object can have
# class : have properties/variables and behaviours/methods

class Person:
    name="prashant" # property 1
    age=20 # property 2

p1=Person() #object creation
p2=Person()
print(p1)
print(p2)

# accessing property by dot(.) operator
print(p1.name)