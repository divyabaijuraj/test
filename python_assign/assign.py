'''






##########################

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list=list(map(lambda x:x*2,my_list))
print(new_list)
####################################

nums=[1,2,3,4,5,6,7,8,9,10]
letters='abcd'

mylist=[num*num for num in nums]
#print(mylist)
my_list=list(map(lambda n:n*n,nums))
#print(my_list)

mylist=[n for n in nums if n%2==0]
#print(mylist)
print(list(filter(lambda n:n%2==0 ,nums)))
#print([(l,n) for l in 'abcd' for n in range(0,4)])
print(filter(lambda  l,n:(l,n)  ,(nums,letters)))

names=['Anu','Hari','Deepa']
age=[13,45,67]

#############################
data1 = (45, 55, [23, 66, 99], (100, -190), -19, -22, (-89, 50, -44))
data2 = []
list1=[]
# print(data2)
for d in data1:

      if (type(d) == tuple or type(d) == list):
           for j in d:
               list1.append(j)

      else:
          list1.append(d)
print(list1)
sum=0
c=0
for i in list1:
   # print(type(i))

    if(i>0 and  len(str(i)) ==2):
        sum=sum+i
        c=c+1

print(sum)
print("avg:",round(sum/c))
########################

max=(lambda x,y:x if x>y else y)
print(max(7,8))


################  filter:filter the given sequence using a function
from functools import reduce
def even(n):
    return n%2==0

nums=[1,2,3,4,5,6,8]

result=list(filter(even,nums))
print(result)

evens=list(filter(lambda n:n%2==0,nums))

#########  map to do operations .
doubles=list(map(lambda n:n*2,evens))
print(doubles)
#########reduce the list by using a function
sum=reduce(lambda a,b:a+b,doubles)
print(sum)


###################  FILE HANDLING
file=open("C:\\Users\\Dell\\Desktop\\test.txt")
#testdata=file.read()
#print(type(testdata))
#list=testdata.split()
#print(type(list))
#print(list[0])
linebyline=file.readline()
print(linebyline[0])
print(linebyline)

'''

###################################
'''
file=open("C:\\Users\\Dell\\Desktop\\test.txt","r")
f=file.readlines()
f1=file.read()
#print(type(f))
#f=open("C:\\Users\\Dell\\Desktop\\testwrite.txt","w")
#list1=['Iam\n','happy\n','always\n']
#for i in list1:
   # f.writelines(i)
#print(f[0])
###using readlines
#for i in f:
  #  print(type(i))
   # print(i)
   # words = i.split()
   # print(words)

#for z in file:
   # words=z.split()
   # print(words)


import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

import datetime

#x = datetime.datetime(2018, 6, 1)
x = datetime.datetime.now()

print(x.strftime("%H"))


###########

import json
x = '{"name":"John", "age":30, "city":"New York"}'
print(type(x))
y = json.loads(x)
print(type(y))
print(y['age'])

##########################

arr=[1,2,3,4]
v=1
x=lambda arr,v:True if v in arr else False
#print(x)

result=x(arr,v)
print(result)
if(result):
   print("X is present")
##########################

 

x=10
y=7
result=lambda x,y:print(x ,"is gereter than", y) if x>y else print(y,"greater than ",x)
print(result(10,15))



even=lambda x: print(x," is Even") if x%2==0 else print(x," is odd")
print(even(5))

################
pat = "asbcklfdmegnot"
str = "eksge"
p=list(pat)
myDict = { p[i] : i for i in range(len(p))}
print(myDict)
str1=list(str)
str1.sort(key = lambda ele : myDict[ele])
print(str1)
str1.reverse()


##################################
count=0
c=0
n=1
sum=0
while(count<=6):
       sum=c+n
       print(sum)
       c=n
       n=sum

       count+=1
##################################

m=1
n=int(input("enter a number"))
for i in range(1,n) :
        if(n%i ==0):
                #print(i)
                m=m*i
                continue
print(m)
if(n==m):
        print("perfect number")
############################################################


#####################

###################################


student = ['sachin','chethan','leela','sharanya','nishanth',' parvathi']
marks=[50,81,90,72,62,85]
dict1=dict(zip(student,marks))
print(dict1)
print({k:v for k,v in dict1.items() if v>80})

input='cat'
i=input.replace('c','b')
print(i)

#############################
dict1={}
input='hello world'

count=0
for i in input:
    if i.isspace():
        pass

    elif i not in dict1:
        dict1.update({i:1})
    else:
        count=count+1
        dict1.update({i:count})
print(dict1)

s='Mr.'
l=['Kiran','Kishore','Ravi']
print([s+x for x in l])
def a_first(a):
    return a[0]
l=[[3,6],[12,20],[6,5]]
#l.sort(key=a_first)
l.sort(key=lambda x:x[0])
print(l)
'''
