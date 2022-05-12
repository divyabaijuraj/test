'''
 data1= [ 100,200,'500','6501',400]
   process the data1 (hint use type and int)
   add all the numbers , find the sum, avg, min and max
   use for loop



data1= [ 100,200,'500','6501',400]
data1_num=[]
#sum=0
c=0
for i in data1:
    if(type(i)==int):
        data1_num.append(i)
        c+=1
       # sum+=i
print("sum : ",sum(data1_num))
print("Average: ",round(sum(data1_num)/c))
print("Minimum: ",min(data1_num))
print("Maximum:",max(data1_num))

2) data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
   note the above tuple could have lists and other tuple
   HINT use type to process using the for loop
   Find the total, max, min, avg


data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
data2_new=[]
for i in data2:
    if(type(i)== list):
        for j in i:
            data2_new+= [j]
            print(data2_new)

    elif (type(i) == tuple):
            for j in i:
               data2_new+= [j]
    else:
        data2_new += [i]

print(sum(data2_new),min(data2_new),max(data2_new),sum(data2_new)/len(data2_new))


import random

def random100():
    l = []
    for i in range(100):
        rc = random.randint(1, 1000)
        # print(rc)
        l.append(rc)
    return l

print(random100())

rand = random100()
# rand.sort()
print('After sorting the list \n\t', rand)

list_500 = []
list_1000 = []
list_odd = []
list_even = []

for i in rand:
    if 0 < i <= 500:
        list_500.append(i)
    else:
        list_1000.append(i)
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)

print('1 to 500 items :\t', list_500)
print('500 to 1000 items :\t', list_1000)
print('even items :\t', list_even)
print('Odd items :\t', list_odd)


print('Maximum number from set of odd list : ', max(list_odd))
print('Minimum number from set of even list : ', min(list_even))
print('Average of set of even list : ', sum(list_even)/len(list_even))

list_odd.sort()
print("\nAverage of last 10 highest numbers of odd set ", sum(list_odd[-10:])/len(list_odd[-10:]))
'''

sentance = input('Enter sentence : ')
sentance1 = sentance.upper()
# print(sentance1)
word = sentance1.split()
# print(word)
vowel = ['A', 'E', 'I', 'O', 'U']
vow = set()
dic = {}
A_M = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I', 'J', 'K', 'L', 'M']
N_Z = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
A_M_List = []
N_Z_List = []
Other_list = []

for i in word:
    if len(i) > 3:
        count = 0
        for j in i:
            if j in vowel:
                count += 1
                if count > 2:
                    vow.add(i)
    if i[0] in A_M:
        A_M_List.append(i)
    elif i[0] in N_Z:
        N_Z_List.append(i)
    else:
        Other_list.append(i)

# print(l1, '\n', l2)
print('Vowel : ', vow)
dic[100] = A_M_List
dic[200] = N_Z_List
dic[300] = Other_list
print(dic)
