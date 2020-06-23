import sys
import random

ask = True

while ask:
    question = input("Ask the Magic 8 Ball a question: (Press Enter To Quit)")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("It is definite")

    elif answers == 2:
        print("The probability is high")

    elif answers == 3:
        print("This is attainable")

    elif answers == 4:
        print("I can't answer that")

    elif answers == 5:
        print("might get lucky")

    elif answers == 6:
        print("It is quite doubtful")

    elif answers == 7:
        print("I think not")

    elif answers == 8:
        print("This will never happen")