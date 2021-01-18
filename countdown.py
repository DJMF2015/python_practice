import random
# for i in range(5):
#     print(5 - i)
# print("happy new year!")

def main():

    number = random.randint(5, 15)
    countdown(number)
    print("Happy New Year!")
#good practice to break code into small units of code
def countdown(n):
    for i in range(n):
        print(n - i)
# call function
main()