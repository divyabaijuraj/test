'''
##Acess the instance variables
class Vehicle:
    def __init__(self,max_speed,min_speed):
        self.maxspeed=max_speed
        self.minspeed=min_speed
model=Vehicle(40,120)
print(model.maxspeed,model.minspeed)
##check a subclass or not

class Base():
    print("in base class")
class  derived(Base) :
    print("derived class")
print(issubclass(derived,Base))
#print(issubclass(Base,derived))

#########################################
class Robot:
    def introduction(self):
        print(self.name)

r1=Robot()
r1.name='Divya'
r1.age=10
print(r1.age)
print(r1.introduction())



class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')

    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')

    def get_gas(self, amount):
        if (self.fuel_level + amount <= self.gas_tank_size):
            self.fuel_level += amount
            print('Added fuel.')
        else:
            print('The tank wont hold that much.')



###########child class

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print('The vehicle is now charged.')

    def fuel_up(self):
        print('This vehicle has no fuel tank!')

electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Car')
electric_vehicle.charge()
electric_vehicle.drive()
electric_vehicle.fuel_up()
print(electric_vehicle.model)

########################BASICS
###instance variable

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age
s1=Student("Anu",12)
print(s1.name," is ",s1.age,"years old")
s2= Student("Amruta", 10)
print(s2.name," is ",s2.age,"years old")

#############
class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"



class Bus(Vehicle):
    pass

V=Bus("School bus",180,12)
print(V.name)
print(V.maxspeed)
print(V.mileage)
print(V.seating_capacity(50))
print(isinstance(V,Vehicle))
help(Vehicle)


class Person:
    def __init__(self,name):
        self.name = name
        #print(self.name)

    def details(self):
        print(self.name)

P1=Person('Deepa')

help(P1.details())

################


###########   MISTAKEN USE OF CLASS variable
class Dog:


    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e=Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play')
print(d.tricks)

######## correct way

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)


class Warehouse:
    purpose='Storage'
    region='west'

w=Warehouse()
print(w.purpose,w.region)

from functools import reduce

l=[[1,2],[3,4]]
print(reduce(lambda a,b:a+b,l))
'''
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2][2][0])

s1={'abc','xyz'}
index=round(int(len(s1))/2)
print(index)
for i in s1:
       print(i[index],end=" ")