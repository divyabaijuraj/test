'''
class NumberSet():
####2 convert the set to the list - call it list1
##### given list2 = [89,23,67,22,100,105,15]

   def set_list(self,num_set):
      print(num_set,"got it")

      list1 = list(num_set)

      list2 = [89, 23, 67, 22, 100, 105, 15]
      ###Process list1 and list2 add elements to list1
      for i in list2:
         list1.append(i)
      print(list1)

      ##minimum in the first 6 elements
      min_l = []
      for i in range(0, 6):
          min_l.append(list1[i])
      print("Lowest in the first 6 elements:",min(min_l))
      ###maximun in the last 5 elements


      max_l = []
      for i in range(-5, 0):
            max_l.append(list1[i])
      print("Highest in the last 5 elements:",max(max_l))

        ## Average of list1 elements

      avg = sum(list1) / len(list1)
      print("Avg:", avg)
      print("Numbers which are above the avg:")
      for num in list1:
            if (num > avg):
                print(num, end=" ")



   def number(self):  ############## 1 input any 5 numbers and store in set ###
        num_set=set()
        s=0
        for i in range(0,5):
           num=int(input("Enter a number:"))

           if num>0:
                num_set.add(num)
           else:
               try:
                   if num < 0:
                      raise ValueError("The value should be greater than zero")
               except ValueError as e:
                      print(e)



        print(num_set)

        ###Find highest number
        print("Maximum value:",max(num_set))
        ###Find Lowest number
        print("Minimum value:",min(num_set))
        #Find sum and average
        print("Avg:",sum(num_set)/5)

        ##sort in reverse order
        print("Reverse order",sorted(num_set,reverse=True))
        self.set_list(num_set)

num_obj=NumberSet()
num_obj.number()

##################################################

class Sets:
    def set1_set2(self):
        st1 = {'Java', 'Python', 'C'}
        st2 = {'SQL', 'Java', 'C#', 'Python'}
        ###Extract those elements from st2 which is not there in st1
        s3 = (st2 - st1)
        print(s3)
        ##Add those elements to st1
        st1.update(s3)
        print("The elements from s2 added to st1:", st1)

        ###remove the skill 'Java' from both st1, st2
        st1.remove('Java')
        print("Java is removed from st1:", st1)
        st2.remove('Java')
        print("Java is removed from st2:", st2)
        print()
        st3 = {'SQLServer', 'ASP.net', 'AWS'}
        # Add st3 into both st1 and st2
        print("Before addition st1:", st1)
        for i in st3:
            st1.add(i)
        print("st3 added in st1:", st1)

        # Add st3 to st2
        print("Before addition st2:", st2)
        for i in st3:
            st2.add(i)
        print("st3 added in st2:", st2)

        ##display the st2 in DESC order
        print(sorted(st2, reverse=True))

obj_set=Sets()
obj_set.set1_set2()

'''

data1=[12,13,24,56,78,23,45,66,23,44]
print(min(data1[0:6]))
print(max(data1[-5:]))