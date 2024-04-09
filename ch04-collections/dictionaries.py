# it is a 'key' and 'value'
# key can be any immutable type

my_dict = {}
#         key : val,  key  : val
grades = {'Ana':'B', 'John':'A+'}
# look up using key
print(grades['Ana'])

dic={'Hussam':'A+', 'Mahmoud':'B-', 'Nahed':'A'}

# add new entry
dic['Dina']='C'
print(dic)

# is key available
print('Hussam' in dic)
print('hussam' in dic)

# removing an entry
del[dic['Mahmoud']]
print(dic)

# keys() and values() methods
print(dic.keys())
print(dic.values())