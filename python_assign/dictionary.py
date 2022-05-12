'''
names=['Anu','Deepa','Appu']
age=[20,34,56]
dict1={}
for i  in range(0,len(age)):
    dict1.update({names[i]:age[i]})

print(dict1)

#################

#max key
dict1={'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
#print(max(dict1,key=dict1.get))
#max value
#print(max(dict1[key] for key in dict1))
values=[]
for k,v in dict1.items():
    values.append(v)
#Get max value
#print(max(values))
max_value=max(values)
#get max key
for k,v in dict1.items():
    if(v==max_value):
        print(k,"$$")
##############
value=list(dict1.values())
key=list(dict1.keys())
print(key[value.index(max(value))])
'''
x='Divya'
y='DIVYA'
if(x.casefold()==y.casefold()):
    print(x)