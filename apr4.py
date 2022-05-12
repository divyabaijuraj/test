##1
'''
n=int(input("Enter a number"))
if(n >=157 and n<= 489 ):
    print(n*3)
else:
    if(n>=670 and n<=978):
         n=n+10
         print(n)
    else:
        n=n+15
        print(n)


##2  and 3

avg,category,yop=input("Enter the average,category and year of passing:").split(" ")
avg=int(avg)
if(category == 'G' and avg>80 and yop=='2021') :
    print("Admission granted")
elif(category == 'D' and avg>68 and (yop=='2019' or yop=='2020' or yop=='2021')):
    print("Admission granted")
elif(category == 'O' and avg>60 and (yop=='2020' or yop=='2021')):
    print("Admission granted")
else:
    #print("Admission not granted")
    income=int(input("Enter the incomeof the parent/guardian"))
    avg=int(input("Enter the average:"))
    year=int(input("Enter year of passing:"))
    if(income<80000 and avg >55 and year>2019):
        print("Admission granted")
    else:
        print("Admission is not granted")

###################################
###1
s='Indian Administrative Service'
l=s.split(" ")   #['India','is','great']
c=len(l)   #3
if c==1:
    if s.isalpha():
        print(s)
else:
    for word in l:
        if word.isalpha():
            print(word[0].upper(), end=" ")

###2




class Student:
    n=3
    dict1 = {}
    c=0

    def get_students(dict1, s):
        #print("class average",s/3 )
        class_avg=s/3
        print(class_avg,"************")
        for k,v in dict1.items():
           # print(k,v)
            if(v[1]>=class_avg):
                print(v[0])

    def __init__(self,n):
        self.n=n
        self.input_data()

    def display_all_details(rollno, name, avg, result):
        l = []
        s = 0

        Student.dict1.update({rollno: [name, avg, result]})

        for v in Student.dict1.values():
             l.append(v[1])
        for mark in l:
            s+=mark
        Student.get_students(Student.dict1,s)
    def process_average(rollno, name, avg):
        if (avg > 0 and avg <= 39):
            result = 'Fail'
        elif (avg >= 40 and avg <= 49):
            result = "Pass"
        elif (avg >= 50 and avg <= 59):
            result = "Second class"
        elif (avg >= 60 and avg <= 74):
            result = "First Class"
        elif (avg >= 75 and avg <= 89):

            result = "distinction"
        elif (avg >=90 and avg <= 100):
            result = "High distinction"
        elif (avg < 0):
            result = 'absent'
        #print(result)
        Student.display_all_details(rollno, name, avg, result)


    def input_data(self):

            rollno = input("Enter the rollno:")
            name = input("Enter the name:")
            avg = int(input("Enter the average:"))

            Student.process_average(rollno, name, avg)
i=0
while (i<=2):
   S=Student(2)
   i+=1
'''
