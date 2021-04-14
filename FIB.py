from sys import argv
from sys import exit


def main():

    if len(argv) != 3:
        exit("Please use proper input")

    print(simulate(int(argv[1]), int(argv[2])))


def simulate(months, size):

    mature = 0
    oldimmature = 0
    newimmature = 1

    for i in range(months - 1):

        oldimmature = newimmature
        newimmature = mature * size
        mature += oldimmature

    return mature + newimmature


if __name__ == "__main__":
    main()
