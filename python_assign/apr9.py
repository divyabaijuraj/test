'''
###April 9 Assignments
class Product:
    def __init__(self):
       self.dict1 = {}

    ##For option 1 Add
    def add(self,key,value):
       if key>0:
               if key in self.dict1.keys():
                   print("Key already exists.Enter another Key")

                   pass
               else:
                   self.dict1.update({key:value})
       else:
         #  Handle the key is entered as negative
         try:

          if key < 0:
             raise ValueError("This is not a positive number!!")
         except ValueError as e:
             print(e)

    ##For option 2 display_all
    def display_all(self):
         print(self.dict1)

    ##For option 3 display_specific item
    def  display_specific(self,key) :
        if key in self.dict1.keys():
            print(self.dict1[key])
        else:
            print("ITEM not found")

    ##For option 4 item_not_available
    def item_not_available(self):
        itm_not_in_store = { }
        for k,v in self.dict1.items():
            if(v[2].casefold() == 'False'.casefold()):
                itm_not_in_store.update({k:v})

                print(itm_not_in_store)



print("Enter your choice:")

value=[]
P1=Product()
d={}
while(True):
    print("1. Add\n2. Display all\n3. display specific item .\n4. Move item NOT avialable\n5. E X I T out of menu\n")
    n = int(input())
    print(n)
   ##For option 1 Add
    if(n==1):

        key=int(input("Enter key value"))
        value=input("Enter  item name, price and availability")
        value=(value.split(" "))
        P1.add(key,value)
    ##For option 2 Display all
    elif(n==2) :
        #print(d)
        P1.display_all()

    ##For option 3 Display specific item
    elif(n==3)  :
        key=int(input("Enter key"))
        P1.display_specific(key)

    ##For option 4 Move item not available
    elif(n==4)   :
        P1.item_not_available()
    ##For option 5 Exit
    elif(n==5) :
        quit()

'''


##################################333333
####2

f_handle=open("C:\\Users\\Dell\\Desktop\\motivational.txt")
#get the contents of a file
contents=f_handle.read()

##get each word of the contents.
words=contents.split(" ")

# get total number of words
print("Number of words:",len(words))
len_word=[]
#get length of each word
for word in words:
    len_word.append(len(word))

#get maximum length
max_len=max(len_word)

#get the word with maximum length
for word in words:
    if len(word) == max_len:
        print("Maximum length word:",word)


#  Display the LAST 10 words from the file
print("Last 10 words of the file:",end=" ")
for i in range(-10,0,1):
    print(words[i],end=' ')


################################################################
###############################    3
class Names:

    name_list=[]
    def display_all(self,name,n):
        #print(name)
        n.add(name)
        l_twochar=[]
        count=0
        for name_str in n:
           #Fetch last two characters of the names
           l_twochar.append(name_str[-2:])

           # names that  starts from R to U
           if(name_str.startswith('R') or name_str.startswith('S') or name_str.startswith('T') or name_str.startswith('U')  ):
                count+=1

           ## names that have  Last name
           l_names=name_str.split(" ")
           if(len(l_names) >1):
               print("Names with last names:",l_names)

        print("Number of names with R/S/T/U:",count)
        print("Last characterts of names: ",l_twochar)




n=set()
while(True):
    name=input("Enter a name")
    if(name.casefold() =='STOP'.casefold()):
        quit()
    else:
        name_obj=Names()
        name_obj.display_all(name,n)



