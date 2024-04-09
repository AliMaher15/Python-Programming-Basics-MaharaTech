# indexing
# start with 0
# Hussam
# 012345
name = "Hussam"
print(name[0])
print(name[5])
# reverse
print(name[-1])
print(name[-2])
# slicing (range-1)
name2 = name[0:2]
print(name2)
print(name[4:6]) # correct
print(name[4:5]) #wrong
# in operator
print("Hu" in name) # True
print("hu" in name) # False
# slicing
print(name[:])
print(name[0:5:2]) # step = 2
# reverse
name3 = name[::-1]
print(name3)