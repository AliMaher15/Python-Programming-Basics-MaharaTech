# store more than 1 element
# in 1 variable

t = ()
print(type(t))

tup = (1,'c',3,'Num')
print(tup)

print(tup[3])
print(tup[2])

tup2 = tup + (20,13)
print(tup2)

# slicing
print(tup2[1:2])
x=('c')
y=('c',) # the , prove it is tuple
print(type(y)," ",type(x))
x1=10,
print(type(x1))

# writing over a tuple
# tuples are immutable
# but can overrite the whole tuple