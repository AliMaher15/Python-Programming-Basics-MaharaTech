# Square brackets
a_list = []
b_list = [2,'a',True]
# recommended to be homogeneous elements
# of the same type

# Lists are mutable
L = [1,2,3]
print(L)
# add element with append()
L.append(7)
print(L)
# add multiple elements with extend([])
L.extend([8,9])
print(L)
# removing elements from lists
# del(L[index])
del(L[2])
print(L)
# remove by value using remove()
L.remove(8)
print(L)
# it remove the first match only
# give error if call it of element not in the list

# extract using pop()
print(L.pop())
print(L)
# pop certain index
L.pop(1) # index 1
print(L)