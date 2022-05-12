'''
f1=open("C:\\Users\\Dell\\Desktop\\test.txt","r")
#contents = f1.read()
#get entire contents
#print(contents)
#get each word
#words=contents.split(' ')

#for word in words:
 #  print(word)
## read first 2 lines

for i in range(2):
    print(f1.readline())
f1.close()

#####Write a Python program to append text to a file and display the text
file1=open("C:\\Users\\Dell\\Desktop\\test.txt","a")
file1.write("\nAppend mode tested.")

file1.close()
'''
############Write a Python program to read last n lines of a file
f_handle=open("C:\\Users\\Dell\\Desktop\\test.txt","r")
#l=len(f_handle.readlines())
n=2
for i in (f_handle.readlines() [-n:]):
    print(i)
    #print(f_handle.readline(2))

    