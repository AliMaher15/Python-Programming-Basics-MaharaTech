S = "show how to split and join"
L = ['show','how','to','split','and','join']

s = "I <3 CS"
print(list(s))
x = list(s)
print(x)

print(s.split('<'))

# concat list into string
# .join(L)
L = ['a','b','c']
print(''.join(L))
print('*'.join(L))

# sort a list with sorted(L), doesn't mutate L
L = [1,5,-3,20,4,9]
print(sorted(L))
print(L)
L.sort() # mutuate L
print(L)
L.reverse()
