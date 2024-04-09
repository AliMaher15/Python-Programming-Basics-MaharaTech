# Global scope: main body of script
# formal parameter: inside function

def f(y):
    x = 1
    x += 1
    print(x) #2

x = 5
f(x)
print(x) #5

def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)