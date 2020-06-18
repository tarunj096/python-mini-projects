import random
roll = True 
print("*********************Dice Rolling Game **********************")

while(roll==True):
    number = random.randint(1,6)
    print("The rolled number on dice is:", number)
    if number == 1:
        print("---------------")
        print("|             |") 
        print("|      0      |")
        print("|             |")
        print("---------------")
    elif number == 2:
        print("---------------")
        print("|      0      |")
        print("|             |")
        print("|      0      |")
        print("---------------")
    elif number == 3:
        print("---------------")
        print("|      0      |")
        print("|             |")
        print("|0           0|")
        print("---------------")
    elif number == 4:
        print("---------------")
        print("|0           0|")
        print("|             |")
        print("|0           0|")
        print("---------------")
    elif number == 5:
        print("---------------")
        print("|0           0|")
        print("|      0      |")
        print("|0           0|")
        print("---------------")
    elif number == 6:
        print("---------------")
        print("|0     0     0|")
        print("|0     0     0|")
        print("|0     0     0|")
        print("---------------")
    inpu = input("Will you roll it once again? y/n:")
    if inpu.lower() == 'n':
        roll=False
    elif inpu.lower() == 'y':
        roll=True
    else:
        
        print("The given response is ivalid! Game is over!!")
        roll=False