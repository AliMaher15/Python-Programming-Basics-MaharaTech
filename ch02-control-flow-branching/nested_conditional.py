x = int(input("Enter an integer:"))
if x%2 == 0 :
    if x%3 == 0 :
        print("divisible by 2 and 3")
    else :
        print("divisible by 2 and not by 3")
elif x%3 == 0 :
    print("divisible by 3 and not by 2")