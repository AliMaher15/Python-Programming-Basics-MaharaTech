# You (the user) thinks of an integer
# between 0 (inclusive) and 100 (not inclusive)

# the computer makes guesses, and you give it
# input is if its guess too high or too low?

# using bisection search, the computer will
# guess the user's secret number!

print("Please think of a number between 0 and 100!")
low = 0
high = 100
medium = (low+high)//2
state = True
while state :
    print("Is your secret number",medium)
    guess = input( "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    if guess == 'c' :
        print("Game over. Your secret number was:",medium)
        state = False
    elif guess == 'h' :
        high = medium
        medium = (low+high)//2
    elif guess == 'l' :
        low = medium
        medium = (low+high)//2
    else :
        print("Sorry, I didn't understand your input.")