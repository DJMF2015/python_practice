import random
#Guess the correct no. 1-10. 3 Attempts.
def generator():
    number = random.randint(1, 10)
    print(f"Number: {number}")
    print("Guess the number 1 - 10. You have 3 attempts")
    print("")
    guessNumber(number)

def guessNumber(number):
    for i in range(3):
        i = int(input("Enter Number: "))
        print("")
        if i < number:
            print("Too small!")
        elif i > number:
            print("Too big!")
        else:
            print(f"Well done! {number} was the correct number")
            print("")
            return None
    print("Sorry you lost you lost")
    print(f"The number was {number}")
    print("")

generator()
