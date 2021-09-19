
import random

print("Welcome to a printing programm.")
high_number = int(input("Low number is 1, what is a high number you with to have? "))
print("Guess a number between 1 and " + str(high_number))
feedback = ''
low = 1

while feedback != 'c' and low != high_number:
    guess = random.randint(low, high_number-1)
    feedback = input(f"Is {guess} too High(H), too low(L), or correct(C)?")
    if ( feedback == 'h' ):
        high_number = guess - 1
    elif( feedback == 'l' ):
        low = guess + 1


print(f"The computer guessed the number, {guess}, correctly!")
        
