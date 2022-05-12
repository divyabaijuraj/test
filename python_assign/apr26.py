'''

def words_dict(list1):
   dict1={}
   ch_A = ([chr(ch) for ch in range(ord('A'), ord('H'))])
   ch_H=[chr(ch) for ch in range(ord('I'), ord('N'))]
   ch_O = [chr(ch) for ch in range(ord('O'), ord('Z'))]
   print(ch_A)
   for i in list1:
       if(i[0] in ch_A):
           dict1.update({100:i})
       elif(i[0] in ch_H)  :
           dict1.update({150: i})
       elif (i[0] in ch_O):
           dict1.update({200: i})
   print(dict1)
def sort_list(sentence):
    print(sentence)
    list1=sentence.upper().split('#')
    list1.sort()
    print(list1)
    words_dict(list1)
sentence='today#is#Tuesday#month#is#April'
sort_list(sentence)
'''
###########################################

s=set()
def avg_num(s):

    list_range=(list(filter(lambda x:x in range(600,801),s)))
    print("Average :",sum(list_range)/len(list_range))


def convert_tuple(s):
    t1 = tuple(s)
    odd = {num for num in s if num % 2 != 0}
    print("sum of odd:", sum(odd))

    even = {num for num in s if num % 2 == 0}
    print("highest even number:", max(even))
    #numbers divisible by 5 or 7

    print("numbers are divisible by 5 as well as 7")
    for n in s:
        if(n>=10  and n<100):
            pass
        else:
            if(n% 5 == 0 and  n % 7 == 0):
                print(n)
    avg_num(s)

def create_set():
    import random
    for i in range(0,10):
        x = random.randint(1,500)
        s.add(x)
    for i in range(0,25):
        x = random.randint(1000,5000)
        s.add(x)

    for i in range(0,15):
        x = random.randint(600,800)
        s.add(x)
    convert_tuple(s)
#print(s)
create_set()





















































































































