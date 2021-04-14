from sys import argv
from sys import exit
import biopython


def main():

    # Ensures correct command line input
    if len(argv) != 3:
        exit("Please use correct input")

    # Reads input into memory
    with open(argv[1], 'r') as file:
        data = file.readlines()

    # Separates two strings from input
    a = data[0]
    b = data[1]

    # Finds differences in strings, being that true equals 1
    hamming = sum(x != y for x, y in zip(a, b))

    # Writes differences to output file
    with open(argv[2], 'w') as file:
        file.write(str(hamming))


if __name__ == "__main__":
    main()
