'''
while
    for
        dict + list
break
...
#if else <= == == = processing

stud_info = {} 
#OR
#stud_details = dict()
roll=0
while roll != -1:
    roll=int(input('enter the roll OR type -1 to EXIT '))
    if roll == -1:
        break
    stud_details = []
    name = input('enter the student name ')
    stud_details.append(name)
    print ('input one by one Phy, chem and maths marks ..... ')
    for i in range(1,4):
        marks = float(input())
        stud_details.append(marks)
    # padding the next 3 element space with 0
    for i in range(4,7):
        stud_details.append(0)
    # add the Key and the value into the dictionary
    stud_info.update({roll:stud_details})
    # OR
    # stud_info [roll] = stud_details
# doing the computation
for k,student_details in stud_info.items():
    student_details[4] = student_details[1]+student_details[2]+student_details[3]
    student_details[5] = student_details[4]/3
    if student_details[5] >=50:
        student_details[6] = 'Pass'
    else:
        student_details[6] = 'Fail'

print ('====displaying the student information ======')
for k,student_details in stud_info.items():
    print ('roll ',k,end=' ')
    for i in range(0,5):
        print(student_details[i],end=' ')
    print('{0:.2f}'.format(student_details[5]),end=' ')
    print('Result:: ',student_details[6],end=' ')
    print()
'''
print("Hi!" *5)