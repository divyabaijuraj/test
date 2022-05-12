'''
a = [1, 24, 3, 43, 66, 5]
#how to get [1,3,5] only as a list
l=[]
for i in a:
    if (i==1 or i==3 or i==5 and i not in l):
        l.append(i)

print(l)

################
#e=[[9,4],[3,5]] how to print e as [9,4,3,5]
e=[[9,4],[3,5]]
e=e[0]+e[1]
print(e)

#write a programe to allow only if the str contains continues same letter. like apple contains two p continuesly
while(True):
    name=input("Enter a string")
    same_letter=False
    if(name.isdigit()):
            print("Enter characters only")
    else:
        for l in name:
                if l*2 in name:
                      # print("Contains same l")
                       same_letter =True
                else:
                    pass
    if not same_letter:
        exit()
    else:
        print("Contains same letter")

###yes we can reverse a tuple
t=(1,2,3)
print(t[::-1])
##############
####Paliandrome

str1='Malayalam'
str1_reverse=str1[::-1]
if(str1.casefold()==str1_reverse.casefold()):
    print("Paliandrome")
################################

string="The day the earth stood still"
print(string.replace('The','an'))
print(string.upper())

'''
from  functools import reduce
e=[[9,4],[3,5]]
print(reduce(lambda a,b: a+b,e))
lis = [1, 3, 5, 6, 2, ]
print(reduce(lambda a,b:a if a>b else b,lis))



