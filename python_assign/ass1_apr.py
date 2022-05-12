
class item:
    def __init__(self,item_id,name,cost_price,item_category):
        self.item_id=item_id
        self.name=name
        self.cost_price=cost_price
        self.item_category=item_category

        def category_A(self, profit):
            self.profit = profit
            sell_price = (self.cost_price) + (self.cost_price * self.profit / 100)
            print('Category A:',sell_price)

        def category_B(self, profit):
            self.profit = profit
            sell_price = (self.cost_price) + (self.cost_price * self.profit / 100)
            print('CategoryB:',sell_price)


        if(self.item_category=='CategoryA'):
            profit=8.5
            category_A(self,profit)
        elif(self.item_category=='CategoryB'):
            profit = 12.5
            category_B(self,profit)



item1=item(101,'Mobile',10000,'CategoryB')
####################################################



########################2 PRIME OR NOT
'''
class  Prime:

    def display(self,n):
        F = False
        self.n=n
        print(self.n)
        if(self.n > 0):
            for i in range(2,n):
                   if(n%i == 0):
                       F=True
                       break

        if(F):
             print("It is not a prime number")
        else:
             print("It is a prime number")

p=Prime()
n=int(input("Enter a number:"))
p.display(n)

#################################

class Pattern:
    def __init__(self,ch,n):
          self.ch=ch
          self.n=n
          print(self.n)


    def display(self):
       # for i in range(0,self.n):
       #     print(self.ch ,end=" ")
        print(self.ch*self.n)


p=Pattern('*',10)
p.display()


class LeapYear:
    def __init__(self,y):
        self.y=y

    def display(self):
        print(self.y)
        if(self.y % 4 ==0):
              print("hi")
              print(self.y%100)
              print(self.y%400)
              if(self.y%100 !=0 or self.y%400 ==0):

                      print("leap year")
              else:
                  print("Not a leap year")
        else:
            print("Not a leap year")

year=int(input("Enter the year:"))
l=LeapYear (year)
l.display()
'''
##################
class Student:
    n = 3
    dict1 = {}

    def display_all_details(rollno, name, avg, result):
        l = []
        s = 0

        Student.dict1.update({rollno: [name, avg, result]})
        print(dict1)

    def process_average(rollno, name, avg):

        # print(rollno,name,avg)
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
        elif (avg < 0):
            result = 'absent'
        Student.display_all_details(rollno, name, avg, result)
        # print(result)

    def input_data(self):
        rollno = input("Enter the rollno:")
        name = input("Enter the name:")
        avg = int(input("Enter the average:"))

        Student.process_average(rollno, name, avg)


S = Student(2)
n = 0
d = S.input_data()

