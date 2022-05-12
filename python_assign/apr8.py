'''
name1 = ['Ashish', 'Manoj', 'Sujata', 'Surya', 'Jayshree', 'Sowmya', 'Pranav']
print('this is going to demo the concept of Error handling ')

try:
    n = int(input('enter a number '))
    print('all is fine ', name1[n])
    a1 = int(input('enter a number '))
    a2 = int(input('enter another number '))
    print(a1 / a2)
except ValueError:
    print('please input number ONLY ')
except IndexError:
    print('the index/subscript must be less than ', len(name1))
except ZeroDivisionError:
    print('divide by ZERO is not allowed ')
else:
    print('GREEN SIGNAL given ')
    print('hey I am here because there were no Error ....All is ok ')
finally:
    print()
    print('Licence Number 34/GG/1211909/QW-SR')
    print('Copyright(C) this code is develpoed by Aroha Technologies ')
    print('All leagl actions will be in the court of Karnataka State ')
'''

#################
class Rabbit:
    __lives_in__ = 'burrow'
    __name__ = 'Rabbit'


class Sheep:
    __lives_in__ = 'pen'
    __name__ = 'Sheep'


class Animal(object):
    pass


class Herbi(Animal):
    __test1__ = 'Deer'
    __test3__ = Rabbit()


class Pet(Herbi):
    __test2__ = 'Grass'


class Alpha(object):
    pass


class Beta(Alpha):
    pass


name1 = ['Ashish', 'Manoj', 'Sujata', 'Surya', 'Jayshree', 'Sowmya', 'Pranav']
print('this is going to demo the concept of Error handling ')

try:
    n = int(input('enter a number '))
    print('all is fine ', name1[n])
    a1 = int(input('enter a number '))
    a2 = int(input('enter another number '))
    print(a1 / a2)
    xyz = 11
    print(xyz)
    nm = {'Anand', 'Kiran', 'Jaya', ['Deepak', 'Akash'], 'Manoj'}
    print('nm is ', nm)
except (ValueError, IndexError):
    print('there is some issue in the code/input ')
except Exception as ee:
    print('nature of issue is ', ee, ' WATCH ::: ', ee.__class__.__name__)
'''
except IndexError:
    print ('the index/subscript must be less than ',len(name1))
except ZeroDivisionError:    
    print ('divide by ZERO is not allowed ')

else:
    print ('GREEN SIGNAL given ')
    print ('hey I am here because there were no Error ....All is ok ')

finally:
    print()
    print ('Licence Number 34/GG/1211909/QW-SR')
    print ('Copyright(C) this code is develpoed by Aroha Technologies ')
    print ('All leagl actions will be in the court of Karnataka State ')
'''
a = Beta()
print(a.__class__, ' is same as ', type(a))

print(a.__class__.__name__)
pt = Pet()
print(pt.__hash__())
print(pt.__test1__, ' eats ', pt.__test2__)
print()
print('this animal called ', pt.__class__.__test3__.__name__, 'lives in ', pt.__test3__.__lives_in__)
print()


class milk:
    data_member3 = 'cat drinks milk'


class kitten:
    data_member2 = milk()


class cat:
    data_member1 = kitten()


obj = cat()
print(obj.data_member1.data_member2.data_member3)
# cat drinks milk
