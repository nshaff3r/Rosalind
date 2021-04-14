from sys import argv
from sys import exit


def main():
    if len(argv) != 3:
        exit("Please use proper input")

    # Runs simulation of sequence
    print(simulate(int(argv[1]), int(argv[2])))


def simulate(months, lifespan):
    mature = 0  # Amount of fully mature rabbits
    oldimmature = 0  # Amount of fully mature rabbits, before calculations
    newimmature = 1  # Amount of immature rabbits
    generations = []  # Keeps track of rabbit generations

    for i in range(months - 1):
        oldimmature = newimmature  # Immature rabbits are now mature
        newimmature = mature  # Each mature rabbit yields 1 immature rabbit
        mature += oldimmature  # Mature rabbits must be added to the mature variable
        generations.append(oldimmature)  # We must keep track of the new rabbits born
        if i >= lifespan - 1:  # By the time we hit the lifespan
            mature -= generations[i - lifespan + 1]  # The rabbits that old die

    return mature + newimmature


if __name__ == "__main__":
    main()
