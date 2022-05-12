"""
#reverse each word of a string
str1="My name is Divya"
list1=str1.split()
print(list1)
new_list=  [word[::-1] for word in list1]
print(new_list)

##############
with open("C:\\Users\\Dell\\Desktop\\file1.txt") as file:
    print(file.read().replace('\n'," "))
########################

ls=[10,20,30,40,50,60,70,80,90,100]
c=0
l=len(ls)
while(c<l):
    if(ls[c] > 50):
        del ls[c]
        l=l-1
    else:
        c=c+1
    print(ls)

###################3333
str1="ABCDEFGH"
str2="CDE"
lstr2=len(str2)
#print(str1.find(str2))
for i in range(len(str1)):
   #print(str1[i:i+3])
   if(str1[i:i+3]==str2):
        print(i)



######reverse of a list
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
###or
list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)

##concatenate two lists  index wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[]
l=len(list1)
l1=len(list2)
for i in range(0,l):
    for j in range(0,l1):
        print(j)
        if(j==i):

            list3.append(list1[i]+(list2[j]))
print(list3)


#square of each number in a list
numbers = [1, 2, 3, 4, 5, 6, 7]
square=[x*x for x in numbers]
print(square)
list1=[]
for i in numbers:
    list1.append(i*i)
print(list1)


###concatenate two lists
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[]
for i in list1:
    for j in list2:
        list3.append(i + j)
print(list3)

####Iterate both lists simultaneously second list in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
print(list2)
for i in list1:
    for j in list2:
        if(list1.index(i)==list2.index(j)):
                 print(str(i), " ",str(j))



#Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1.remove("")
print(list1)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
 """
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:-5])

