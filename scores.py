def main():
    score1 = int(input("Score 1: "))
    score2 = int(input("Score 2: "))
    score3 = int(input("Score 3: "))

    print_score(score1)
    print_score(score2)
    print_score(score3)

    # for i in range(score1):
    #     print("#", end="")
    # print()

    # for i in range(score2):
    #     print("#", end="")
    # print()

    # for i in range(score3):
    #     print("#", end="")
    # print()


def print_score(n):
    for i in range(n):
          print("#", end="")
    print()

main()