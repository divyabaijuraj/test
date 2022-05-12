# is handled by the lead - Hari Kishore
class Car(object):

    def factory(type):

        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()
        if type == 'ECar':
            return ECar()

    factory = staticmethod(factory)


# code Sai Deep
class Racecar(Car):
    def drive(self):
        print("Racecar driving.")


# code Divya
class Van(Car):
    def drive(self):
        print("Van driving.")


# code Ramya
class ECar(Car):
    def drive(self):
        print('Fun to drive a e-car ....non-polluting ')


# Create object using factory.
# is handled by the lead - Hari Kishore
try:
    choice = int(input('Enter choice 1. for RaceCar  2. Van 3. ECar '))

    if choice == 1:
        obj = Car.factory("Racecar")
        print(obj)
    elif choice == 2:
        obj = Car.factory('Van')
    elif choice == 3:
        obj = Car.factory('ECar')

    obj.drive()
except Exception:
    print('wrong choice !! ')