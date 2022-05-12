'''
##### 1
print("Enter 5 numbers")
s=0
count=0
list1=[]
for i in range(0,5):
        n=input()

        if(len(n) ==3):
                s=s+int(n)
                count+=1
                list1.append(n)

print("Higher value:",max(list1))
print("Lower value:",min(list1))
print("Sum:",s)
print("Average:",s/count)

################  2

n=1
s=0
c=0
l=[]

while(n<=5):
    num=input("Enter the number:")
    n=n+1
    if(int(num)%6 ==0 and int(num)%7 ==0):
        print("Divisible by 6 and 7:",num)

    if(len(num)==3):
        l.append(num)
        s=s+int(num)
        c=c+1
print("sum:",s)
print("avg:",s/c)
print(max(l),min(l))

##############  3

data1 = [34, 389, 425, 225, 12, 56, 199, 305, 78, 121, 33, 400, 22, 90]
l=[]
for i in data1:
    if(len(str(i)) == 3 and i<300):
        l.append(i)

print(max(l))

################  4

data1 = (10,22,45,39,41,5,100,28,38,31)

data2=list(data1)
data2.sort()
print(data2)
print(max(data2),min(data2),data2[-2],data2[1])

#################### 5

a=199
b=77
c=6
s=0
data1 = {89,44,77,234,199,190,180,6,17,16}

if a and b and c  in data1:
    #print("done")
    #data1.difference_update({199,77,6})
    data1.remove(a)
    data1.remove(b)
    data1.remove(c)
    #print(data1)

print(data1)
for i in data1:
    s=s+i
print("sum:",s)
print("AVERAGE:",s/len(data1))

######################## 6

keys=[]
data1 = { 45: 'Kishore', 89 : 'Lata', 199 : 'Asha', 345 : 'Mohan'}
for key,value in data1.items():
        if key in data1.keys():
                keys.append(key)
for k in keys:
        data1.pop(k)
else:
        key=input("Enter the key:")
        value=data1.get(key)
        if value is None:
               v =input("Enter a value for tjhe given key:")
               data1.update({key:v})
print(data1)

############### 7
data1 = {10: -567, 25: 775, 39: -121, 45: 1000,23:980,14:345,20:1200}
sum=0
c=0
l=[]
for k,v in data1.items():

        if(v>=0 ):


                if(v>=850 and v<=1000):
                        pass
                else:
                        l.append(v)
                        sum=sum+v
                        c = c + 1


print("The sum is:",sum)
print("The average is:",sum/c)
print("The highest number:",max(l))
print("The lowest number:",min(l))


################29 march
###1
def display_amount(si,p):
    a=si+p
    print("Amount:",a)
def compute_interest(p,t,r):
    si=(p*t*r)/100
    print("simple interest:",si)
    display_amount(si,p)
def input_data():
    p=float(input("Enter Principal Amount:"))
    t=float(input("Enter the time period :"))
    r=float(input("Enter the rate of interest:"))
    compute_interest(p,t,r)

input_data()
 ###############################################
'''

###2
error_msg=''

while(True):

    name = input("Wish to quit or not Enter yes or No:")
    print(name)
    if(name.lower()=='yes'):
        exit()
    else:
        prod_dict={ 1000: (72.55,10), 2000 : (56.25,5), 3000: (25.25,15) }
        prod_name = { 1000: 'Toothpaste', 2000 : 'Soap' , 3000 : 'Campor' }
        pname=input("Enter the product name:")
        Key=0
        q=0
        l=[]
        for k,v in prod_name.items():
          if pname.lower() == v.lower():
            Key=k

          else:

               error_msg="Enter a valid product name"
        quantity = input("Enter the quantity of the item to buy:")
        q = quantity
        q1=0
        for k,v in prod_dict.items():
            if(Key==k):
                #print(v)
                q1=int(v[1])

        if int(quantity) <= q1:
            print("The quantity is available")

            for k in prod_dict.keys():
                    if(Key==k):
                           l=(prod_dict.get(k))
                           l=list(l)
                           new_quan= int(l[1]) -int(q)
                           l.pop(1)

                           l.insert(1,new_quan)
                           t = tuple(l)
                           #print(t)
                           prod_dict.update({k:t})

                           print(prod_dict)
        else:
            print('Asked qty is NOT available')

################### 3
'''
set1 = { 100, 560,220, 565,121, 10, 15}
list1 = [890,560,-220, -565, 12,-10 , 14,22,15]
l=[]
c=0
for i in list1:
    l.append(abs(i))
#print(l)
for i in set1:
 # print(i)
  if i in l:
        l.remove(i)
        c=c+1
        if(c >= 4 ):
            print(l)
            quit()

print(l)



'''
