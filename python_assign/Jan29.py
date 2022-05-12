"""
fruits=[]
fruits=input("Enter 5 names:")
places=[]
places=input("Enter 3 names:")
fruits=set(fruits)
places=set(places)
set_items=fruits.union(places)
tuple1=tuple(set_items)

for value in tuple1:
    print(tuple1.index(value),value)
    """
###2

students={
    1:["Anu",40,50,80],
    2:["Deepa",60,77,86],
    3:["Rishika",69,45,90],
    4:["Arjun",52,74,81],
    5:["Hari",84,52,79]
}
#for i in range(0,5):
 #       print(students.values())
c=1
marks=[]

while (c<=5):
    str1 = []
    numbers = []
    for i in students[c]:

        if(type(i) == str):
                     str1.append(i)
        else:
                  numbers.append(i)
    marks.append(numbers)

    c+=1
str(marks)
l=len(marks)
for len1 in range(0,len(marks))  :
    sum=0
    lst_sum=[]
    for j in range(0,len(marks[0])):
        sum= sum+(marks[len1][j])
    print(max(str(sum)))




