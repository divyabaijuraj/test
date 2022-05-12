'''
class Name:
    def check_vowel(self,name):
        self.name=name
        #print(self.name)
        vowels=['a','e','i','o','u']
        if(len(self.name) <8):
            print("Cannot perform the action")
        else:
            for i in self.name:
                 if (self.name.index(i)==8):
                      # print(i)
                       if i in vowels:
                           print("8th letter is:",i)
                       else:
                           print("8th letter is not vowel")
name=input("Enter the name")
n=Name()
n.check_vowel(name)
#######################################
#2
class Sentence:
    def wordCheck(self,s1,w):
        self.s1=s1
        words=self.s1.lower().split(" ")
        print(words)
        if w.lower() in words:
            print("Number of words present:",words.count(w))
            print("First occurance of the word in the sentence:",self.s1.lower().index(w.lower()))

s1=input("Enter a sentence:")
w=input("Enter the word to find:")
s=Sentence()
s.wordCheck(s1,w)


##3

class EnterName:
    def checkName(self,name):
        self.name=name
        print(self.name.lower())
        print(self.name.upper())
        print(self.name.capitalize())

name='diVyA'
name1=EnterName()
name1.checkName(name)
#################

##4
class Phone:
    def Phonenum(self,phone1):
        self.phone1=phone1
        if (len(self.phone1)<10):
            print("Invalid Phone Number")
        else:
            if (self.phone1.endswith('8') or  self.phone1.endswith('5')):
                print("True")
            else:
                print("False")

phoneno='9923412344'
phone1=Phone()
phone1.Phonenum(phoneno)

######################
##4
class Phone:
    def Phonenum(self,phone1):
        self.phone1=phone1
        if (len(self.phone1)<10):
            print("Invalid Phone Number")
        else:
            if (self.phone1.endswith('8') or  self.phone1.endswith('5')):
                print("True")
            else:
                print("False")

phoneno='9923412344'
phone1=Phone()
phone1.Phonenum(phoneno)
#####################

##########5
class Sentence:
    def wordCheck(self,name1,word1):
        self.name1=name1
        words=self.name1.lower().split(",")
        #print(words)
        #print(word1)
        if word1.lower() in words:
           print("The matching word is :",word1)

name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
word1 ='VEENA'
s=Sentence()
s.wordCheck(name1,word1)

###################

class Year:
    def calculate(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
        months=[4,6,9,11]

        if((self.d>=1 and self.d<=31) and (self.m>0 and self.m<=12)):
            if(m in months ):
                if(self.d>=1 and self.d<=30):
                    print("valid day")
                else:
                    print("invalid day")
            else:
                print(type(self.y))
                if ((self.y % 400 == 0 and  self.y % 100 == 0) or(self.y % 100 != 0 and self.y % 4==0 )):

                    if (d >= 1 and d <= 29):
                        print("valid")

                else:
                    print("invalid")



d=int(input("Enter the day in digit"))
m=int(input("Enter the month"))
y=int(input("Enter the year"))
y1=Year()
y1.calculate(d,m,y)

#########################################
##7
class LPG:
    def __init__(self,category,qty):
        self.category=category
        self.qty=qty
        print(self.category)
        if(self.qty >=1):
            if(self.category.lower() == 'commercial' ):
                price=1450
                if self.qty > 6:
                    print("Cannot proceed")
                elif self.qty >3 and self.qty<=6:
                    discount=price*(5/100)
                    bill=(self.qty*price) - discount
                    print(bill)

                else:
                    bill = self.qty * price
                    print(bill)
            elif self.category.lower() =='domestic' :
                price=950
                bill = self.qty*price
                print(bill)
            else:
                print("Enter valid category")
        else:
            print("Enter valid quantity ")


category=input("Enter category")
qty=int(input("Enter quantity"))
c1=LPG(category,qty)

#############################################33

###8


class Digit:
    def checkNum(self,n):
            c=0
            ##last digit of the number is obtained by using the modulus operator

            ##Each time a digit is obtained, the count value is incremented.This loop terminates when the value of the number is 0.

            while (n > 0):
                c= c + 1
                n = n // 10
                print(n)
            print("The number of digits in the number are:", c)
            if (c == 1):
                print("single digit number")
            elif (c == 2):
                print("doubledigit number")
            elif (c == 3):
                print("Three digit number")

            elif (c == 4):
                print("Four digit number")
            elif (c == 5):
                print("Five digit number")
            elif (c >= 6):
                print("Its a big number")


n=int(input("Enter a number"))
num1=Digit()
num1.checkNum(n)


'''

##################################

class Sentence:
    def wordCheck(self,s1,w):
        self.s1=s1
        words=self.s1.lower().split(" ")
        #print(words)
        search_word=w.lower()
        #print(search_word)
        if (search_word in words):

            print("Number of words present:", words.count(search_word))
            print("First occurance of the word in the sentence:", self.s1.lower().index(search_word))
        else:
            print("Matching word doesn't find")

s1=input("Enter a sentence:")
w=input("Enter the word to find:")
s=Sentence()
s.wordCheck(s1,w)

