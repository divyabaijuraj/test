#######  Assignment1
#1
x= "Python contains different compound data types"
print(x.split("o"))
#2
list_fruits=["Banana","Mango","Orange","Apple","Grapes"]
print(tuple(list_fruits))
print(set(list_fruits))

#3
str="Python Programming"
print(str.lower())
print(str.upper())

#4

student={'name':'John','city':'Austin','birth_year':2002,'height':175}
print(student)

#5
###List operations-  append,sort ad pop
states=['Karnataka','Kerala','Maharashtra','TamilNadu']
states.append('Rajastan')
print(states)
states.sort()
print(states)
states.pop()
print(states)
###set operations- add,update,remove
set_num={1,2,3,4}
set_num.add(5)
print(set_num)
set_num.update([3,4])
print(set_num)
set_num.remove(2)
print(set_num)

##tuple add,slice,multiply
tuple1=(1,2,3,4)
tuple1=tuple1+(9,)
print(tuple1)
print(tuple1[1:3])
print(tuple1*3)
## dictionary update,add,pop
dict1={'name':'Divya','age':38}
dict1['name'] = 'Deepa'
print(dict1)
dict1['place']='Bangalore'
print(dict1)
dict1.pop('name')
print(dict1)