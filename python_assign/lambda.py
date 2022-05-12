'''
##52. Write a Python program to remove None value from a given list using lambda function
l=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
result=filter(lambda x:x is not None ,l)
print(list(result))


# 51. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.

def max_min_list_tuples(ltup):
    return_max = max(ltup, key = lambda item: item[1])[1]
    return_min= min(ltup,key=lambda item:item[1])[1]
    print(return_max,return_min)

    #return_max = max(class_students,key=lambda item:item[1])[1]
    #return_min = min(class_students,key=lambda item:item[1])[1]

    #return return_max, return_min
ltup= [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
max_min_list_tuples(ltup)

#50 Write a Python program to remove specific words from a given list using lambda

l=['orange', 'red', 'green', 'blue', 'white', 'black']
rwords=['orange', 'black']
for i in l:
    if i in rwords:
        l.remove(i)
#print(l)
##lambda
#print(list(filter(lambda i:i not in rwords,l)))
#list comprehension
print([x for x in l if all(word not in l for word in rwords)])

#49 49. Write a Python program to count the occurrences of the items in a given list using lambda
from collections import Counter

l=[2,3,4,7,2,4,8,9]
num=set(l)
print(num)
print(Counter(l))
dict1= {}

count=0
x=''
#for i in l:
   # x=i
    #print(i,":",l.count(i),end=" ")
for i in l:
    if i in num:
        print(i,l.count(i))



l1=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

result=sorted(l1,key=lambda x:int(x))
print(result)
'''
##47. Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
l=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
result=sorted(l,key=lambda  x:type(x)==str )
print(result)

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
for key in sorted(color_dict.keys()):
    print(key,color_dict[key])
