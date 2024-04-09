# function without arguments or return
def printHello() :
    print("Hello from function printHello")

printHello()

def printSum(num1, num2):
    print(num1+num2)

printSum(5,10)
x = 20
y = 30
printSum(x,y)

# no arg but with return
def pi():
    return 22/7

circ = 2 * 7 * pi()
print(circ)

# arg and return
def isEven(num):
    return num%2==0

print(isEven(2))
print(isEven(3))

# Docstrings
def isOdd(num):
    """
    this function is used to tell if the given number is odd
    input: num, Type: Integer
    output: Boolean
    """
    return num%2!=0

print(isOdd(3))