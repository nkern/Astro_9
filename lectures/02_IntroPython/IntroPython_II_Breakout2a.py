# magic 8-ball
import random

while True:
    # ask question
    question = input("Ask a yes-or-no question: ")

    # generate random
    rand = random.randint(1, 8)

    # answer
    if rand == 8:
        print("impossible")
    elif rand == 7:
        print("highly implausible")
    elif rand == 6:
        print("unlikely")
    elif rand == 5:
        print("who knows?")
    elif rand == 4:
        print("50-50")
    elif rand == 3:
        print("likely")
    elif rand == 2:
        print("most probably")
    elif rand == 1:
        print("absolutely")

    again = input("Ask another question? [y/n] ")
    if again != 'y':
        break









