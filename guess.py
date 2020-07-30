import random

num = random.randint(1,15)
guess = int(input("Enter a number between 1 and 15:"))

while num!=guess:
    if guess > num and guess <= 15 and guess > 0:
        print("The number guessed is too high")
        guess = int(input("Enter a number between 1 and 15:")) 
    elif guess < num and guess <= 15 and guess > 0:
        print("The number guessed is too low")
        guess = int(input("Enter a number between 1 and 15:"))
    else:
        print("The number you guessed isn't between in 1 and 15, Hence it's wrong!")
        guess = int(input("Enter a number between 1 and 15:"))
print("Congratulations! You guessed it!")
