'''
###  Add all the digits oif a number
num=int(input("Enter a number"))
s = 0
while (num != 0):

       s = s + (num % 10)
       print("sum:",s)
       num = num // 10
       print("num:",num)

print("sum of digits:",s)

##############  2

dict2={10:'Anu',20:'Ram'}
keys=set(dict2.keys())
print(keys)
for key in keys:
      if key in dict2.keys():
             dict2.pop(key)
            # print(dict2)
print(dict2)

############################
l=[12,3.5,'abc',34,6.7,'abt',8]
for i in l:

   if(type(i)== int):
          print(i)

   elif(type(i)==float):
          print(i)




flag=False
l=set()
for i in range(10,20):
  for j in range(2,int(i/2)+1):
       if(i%j ==0):
             break
       else:
              l.add(i)
print((l))


##########################
list1=[1,0,1,1,0,0]
l=['True' if x==1  else 'False' for x in list1 ]
print(l)
#str1=' '
#print(str1.join(str(list1)))
#print(str1)

##############
s={'anu','deepa'}
for i in s:
    print(i[-1])


str1="I get it done"
print(str1.title())
print(str1.swapcase())

class Test:
   x=10
   def __init__(self):
     self.y=20
t1=Test()
print(t1.x,t1.y)
print(Test.x,t1.y)
Test.x=100
t1.y=50
print(t1.x,t1.y)
##############
n=234
c=0
while(n>0):
    dgt=n%10
    n=n//10
    c+=1
    print(dgt,"digit")

    print(n,"num")
    print(c)

    #########################333
        i=213
        count = 0
        while(i>0):
            digit=i%10
            i=i//10
            count+=1

'''
num=10
print (bin(num).count("1"))