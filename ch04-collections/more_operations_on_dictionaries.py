d1 = {'A':10,'B':20}
print(d1)

# iterate over dictionary
for key in d1:
    print(key+':'+str(d1[key]))

d2 = {'C':30,'D':40}
# modifying values
d1['A']=100
print(d1)
print(d1.get('A'))
print(d1.get('F'))
print(d1.get('F',-1))

# update a dictionary
d1['F']=90
d1.update(d2)
print(d1)