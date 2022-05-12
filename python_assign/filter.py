### Filter---it filters a given sequence with the help of a function.

###sequence can be a list,set,tuple
l1=[[1,2],[3,4]]

seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = map(lambda x: x % 2 != 0, seq)
print(list(result))

###filter results in [1, 3, 5, 13]

###MAP
# results in [False, True, False, True, True, False, True]
##   Returns a list of the results after applying the given function
###  to each item of a given iterable (list, tuple etc.)
###  The reduce(fun,seq)