'''
####highest salary,and lowest salary
salary=[('Sunil',26500),('Anil',35000)]
listn=[]
lists=[]
dict1={}
for i in salary:
   #print(i[1])
   listn.append(i[0])
   lists.append(str(i[1]))
dict1=dict(zip(listn,lists))
#print(dict1)
#get value
print(max(dict1[key] for key in dict1))
#get key
print (max((dict1),key=dict1.get),"is getting highest salary")
print (min((dict1),key=dict1.get),"is getting lowest salary")

####find highest number
Data1={125,600,250,350,444,90,86,120,37,89,150,125}
print(max(Data1))
sum=0
count=0
for i in Data1:
    if(i>=200 and i<=350):
        count+=1
        sum+=i
        #print(sum)

    else:
        pass
print(sum)
if (count > 0):
       print (sum/count,"Average: ")
#print(sum)

#print(sum(Data1))





###checxk duplicate
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
       # print(l1)
    else:
        print(i,end=' ')
###number of time each value repeated in a alist

from collections import Counter
my_dict={}
l=[1,2,3,4,5,2,3,4,7,9,5]
my_dict = dict(Counter(l))

print(my_dict)

###process the files and count the number of words and number of characters.
file1=open("C:\\Users\\Dell\\Desktop\\test.txt")
str1=file1.read()

list1=str1.split(' ')
print("The words in a string: ",len(list1))
c=0
for i in list1:
   for j in i:
      # print(j)
       c=c+1

print("number of letters:",c)

#############Procee to find the number of times a substring prestent in the string

str1="Hello how are you?How is the work?Sunil,I hope Sunil is fine"
find_str="Sunil"
print("The number of occurance of Sunil: ",str1.count(find_str))
print(str1.replace(find_str,'Ganesh Kumar'))




############## find the average second  highest and third lowest

Data2={1000:(12,45,66),2500:(100,37,78,22),3000:(50,60)}
list1=[]
for k,v in Data2.items():
    list1.append(v)

print(list1)
sum=0
count=0
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
        sum=sum+j
        count=count+1
print(sum)
print(count)
print("The average is :",round(sum/count))
list2.sort()
print(list2)
print(list2[-2],list2[2])


#############
dict1={}
salary=[('Sunil',26500),('Anil',35000)]
dict1=(dict(salary))
#print (max((dict1),key=dict1.get),"is getting highest salary")
print(min((dict1),key=dict1.get))
print(max((dict1),key=dict1.get))


########## EXTRA questions
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}
del D['name']

D['name']='Bob'
print(D)

L = ['ReD', 'GrEeN', 'BlUe']
D={c.lower():c.upper() for c in L }
print(D)
####################
lnum = []
while (True):

    n = int(input("Enter a number:"))
    if (n >= 0):
        lnum.append(n)
        print(lnum)

    else:
        exit()
print("testing")
print(lnum)
l = len(lnum) / 2
l1 = lnum[2:]
sum = 0
count = 0
for i in l1:
            sum += i
            print("Sum is", sum)
            print("Average is", sum / count)


###################

num=int(input("How many names u want to enter :"))
S=set()
for i in range(0,num):
   names=input("Enter the names:")
   S.add(names)
print(S)
####################

d={}
n=0
while(n<2):

    accountno=int(input("Enter the account number:"))
    balance=int(input("Enter the balance:"))
    print(d.get(accountno))
    if accountno in d:
        exit()
    else:
       d.update({accountno:balance})
    n=n+1


print(d)
lists=[]
for k,v in d.items():
    lists.append(v)
print(sum(lists),max(lists),min(lists),(sum(lists)/len(lists)))

###########################

set1={10,45,67,78,199,200}
set2={333,22,55,199,200,39}
print(set1.intersection(set2))


############################
dict1={1000:'Sanjay-P',2001:'Ganesh-T'}
dict2={550:'Pooja-T',435:'Uday-P'}
lst1=['T','P']
dictp={}
dictt={}
for k,v in dict1.items():
    if(v.endswith('T')):
        dictt.update({k:v})
    else:
        dictp.update({k:v})
for k,v in dict2.items():
    if(v.endswith('T')):
        dictt.update({k:v})
    else:
        dictp.update({k:v})

print(dictt)
print(dictp)

####################
D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
#selectedKeys = [0, 2, 5]
#print({k:D[k] for k in selectedKeys})
removeKeys = [0, 2, 5]
X = {k: D[k] for k in D.keys() - removeKeys}
print(X)

##################
D={'name':'Bob','age':10}
#v=D.pop('name')
#print(v)
D.popitem()
print(D)


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

################################
l=[]
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

dict1={}
keys = ["name", "salary"]
for k in keys:
   dict1.update({k:sample_dict.pop(k)})
print(sample_dict)
print(dict1)

#################
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("yes")

##############
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict.pop('city')
print(sample_dict)
sample_dict['location']='New York'
print(sample_dict)

####################
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict, key=sample_dict.get))

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)

#######################


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['backpack'].sort()
print(inventory)

################
from collections import OrderedDict
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

for i in sorted(sample_dict):
    print(i,sample_dict[i])

dict1 = OrderedDict(sorted(sample_dict.items()))
print(dict1)
###################

from collections import Counter
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(Counter(sample_dict))

dict={0:'A',1:'B',3:'C',2:'D'}
select_keys=[2,3]
#print({k:dict[k] for k in select_keys })
for i in sorted (dict.keys()) :
     print(i, end = " ")


####################
list1=[]
d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : 12,
        'D' : [7, 8, 9, 6, 4] }

#print(d)
count=0
str1=""
for v in d.values():
    str1=str1+str(v)
    count+=1

dict = {0: 'A', 1: 'B', 3: 'D', 2: 'C'}
select_keys = [2, 3]
# print({k:dict[k] for k in select_keys })
for i in sorted(dict.values()):
    print(i, end=" ")

emp={'anu':30000,'ammu':45000,'reshma':50000,'subha':79000}
list1=[]
list2=[]
min_value=min(emp,key=emp.get)
print(min_value)
print(emp[min_value])
max_value=max(emp,key=emp.get)
print(max_value,':', emp[max_value])
for k,v in emp.items():
    list1.append(k)
    list2.append(v)
print(list1)
print(list2)

str1='Divya-P'
pos=str1.index('-')
print(pos)
print(str1[0:-2])
################
S = {'red', 'green', 'blue'}
S.add('orange')
print(S)
S.pop()
print(S)

S = ('red', 'green', 'blue')



print(S)

S = 'BigBiggerBiggest'
x = S.count('Big')
print(x)





country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
print(country_code.get('US'),"Not present")

################
S = 'Bob is a Developer at ABC'
x = S.index('Developer')
print(x)

####### Centered####
S = 'Centered'
x = S.center(14)
print(x)


dict1={}
phonebook={('sam',99912222),('tom',11122222),('harry',12299933)}
print(phonebook)
list1=list(phonebook)
#print(list1)
dict1=dict(list1)
#del dict1['sam']
x=dict1.pop('sam')
print(x)


key=input("Enter name:")
if key  in dict1.keys():
    print(key,":",dict1[key])
else:
    print("Not found")
###############################
a=1
while(a%5!=0):
    a=a+3
b=1
while not (a%2 ==b):
    b=b+a
    a=a+b
    break
print(a,b)


################
list1=[]
order1={'O100':4500,'O345':3300,'O1230':5400,'O2001':9888,'O334':2443,'O2289':3409}
ord_set_ignore={'O100','O2001','O334'}
dict1_cancel= {}
dict2={}

for k,v in order1.items():
    if k in ord_set_ignore:
        dict1_cancel.update({k:order1[k]})

    else:
        dict2.update({k:order1[k]})
        list1.append(v)
print(dict1_cancel)
print(dict2)
print("total amount:",sum(list1))
print("avg amount:",round(sum(list1)/len(list1)))
print(max(list1))
print("Order with min value in cancelled orders:",min((dict1_cancel),key=dict1_cancel.get))
print("Order with max value in orders:",max((dict2),key=dict2.get))
print(max(dict2[key] for key in dict2))
print(min(dict1_cancel[key] for key in dict1_cancel))

'''
file=open("C:\\Users\\Dell\\Desktop\\test.txt",'r')
c=0
#for line in file:
   # if(line[0] not in 'T'):
     #     c+=1
#print("Toatal number of lines",c)

#data1=file.read()
#print(data1.count('done'))
'''
data=file.read()
words=data.split(' ')
print(words.count("The"))
for word in words:
   print(word)
   if(word[-1]=='e'):
       c=c+1
print(c)


##############################
count=0
file=open("C:\\Users\\Dell\\Desktop\\test.txt",'r')
data=file.read()
for letter in data:
    if(letter.isupper()):
        count+=0
print(count)

#############################   LIST

L=[1,2,3,4,5]
L.reverse()
print(L)
L=['red', 'green', 'blue', 'orange']
L.sort(reverse=True)
print(L)
L.sort(key=len)
print(L)

from collections import OrderedDict
dict1={}
L = [('Zam', 30),
     ('Sam', 35),
     ('Max', 25)]
L.sort()
print(L)
dict1 =dict(L)
dict1=OrderedDict(sorted(dict1.items()))
print(dict1)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i in list1:
    for j in list2:
        if(list1.index(i)==list2.index(j)):
            print(i+j)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        print(i+j)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
#print(list(zip(list1,list2)))

for i in list1:
    for j in list2:
      #  print(i,j)
        if (list1.index(i) == list2.index(j)):
            print(i, j)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
#res = list(filter(None, list1))
#res=list(filter(None,list1))
#print(res)
l2=[]
for l in list1:
    if(l != ""):
        l2.append(l)
print(l2)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
#################################
list1 = [5, 20, 15, 20, 25, 50, 20]
c=list1.count(20)
print(c)
for i in range(0,3):
    list1.remove(20)
print(list1)
for i in list1:
    if(i!=20):
        print(i)
#########################

count=0
tuple1 = (45, 45, 45, 45)
l=0
print(tuple1.count(45))


sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
setlist=set(sample_list)
print(setlist)

sample_set.update(sample_list)
print(sample_set)
 
###################
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))
##################
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

###################

command=[]
list1=[]
#while(c<=12):
str1=input("")


command=str1.split(' ')
if(len(command)==3):
      print(command[0],command[1],command[2])
      if(command[0]=='insert'):
          list1.insert(int(command[1]),command[2])

elif(len(command) == 2):
    print(command[0], command[1])
elif(len(command) == 1):
    print(command[0])
print(list1)

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

sampleDict1 = {
  "name": "Nami",
  "age":36,
  "salary": 800000,
  "city": "Kerala" }


keys = ["name", "salary"]
#print({k:sampleDict[k] for k in keys})
for i in sorted(sampleDict.keys()):
    print(i)


L = [1,9,5,(1, 2, 3),[4, 5, 6],[7, 8, 9]]
for list in L:
    for number in list:
        print(number, end=' ')
'''
l = [1,2,[3,4]]
e=l[0]
#if isinstance(l,list):
  #  print(len(l))
my_tuples = [12,13,[1, 2, 3], ('a', 'b', 'c', 'd', 'e'), (True, False), 'qwerty']
for i in my_tuples:
  #  print(type(i))
  if(type(i)=='list'):
      print("test")