# if condition :
#    break
# exit loop and continue the rest of the code

mysum = 0
for i in range(5,11,2) : # 5, 7, 9
    mysum += i
    if mysum == 5 :
        break
print(mysum)