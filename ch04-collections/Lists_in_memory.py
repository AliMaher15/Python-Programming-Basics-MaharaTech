l1 = [1,2,3]
l2 = [1,2,3]

l1[0] = 5

print(l1," ",l2)

# same memory location
l1 = [4,5,6]
l2 = l1 #not a copy, pointer to same memory location
l1[1]=10
print(l1," ",l2)
l2[2]=0
print(l1," ",l2)

# cloning a list
l1 = [10,20,30]
l2 = l1[:]
print(l1," ",l2)
l1[1]=40
print(l1," ",l2)

# sorting lists
l1 = [5,-2,10]
l2 = sorted(l1)
print(l1," ",l2)