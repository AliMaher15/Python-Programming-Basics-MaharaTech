# swap
x = 5
y = 20
(x,y) = (y,x)
print(x," ",y)
# return more than one value
def quotient_and_remainder(x,y):
    q=x//y
    r=x%y
    return(q,r) #output

print(quotient_and_remainder(9,6))