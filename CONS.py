from sys import argv
from sys import exit
from itertools import islice
import numpy as np
import time

start_time = time.time()
# Stores labels and sequences
dataset = {}


def main():
    # Ensures proper command line arguments
    if len(argv) != 3:
        exit("Please use proper input")

    # Reads file into string
    with open(argv[1], 'r') as file:
        data = file.readlines()

    # Organizes data into dict dataset
    length = read(data)

    # Creates profile matrix
    profile = np.zeros([4, length])

    # Dict for matching bases and their matrix row
    letters = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Adds base frequency to profile matrix
    for sequence in dataset:
        for i in range(length):
            base = dataset[sequence][i]
            profile[letters[base]][i] += 1

    # Finds matrix row containing the max in each column
    intcstring = np.argmax(profile, 0)

    # For converting row from number to letter
    strcstring = ""

    # Reverses dictionary for converting numbers to letters
    letters = dict(map(reversed, letters.items()))

    # Converts numbers in intcstring to letters
    for number in intcstring:
        strcstring += letters[number]

    # Writes result to file
    with open(argv[2], 'w') as file:
       file.write(strcstring)

    print("--- %s seconds ---" % (time.time() - start_time))


def read(file):
    beginning = 0
    label = None  # For first iteration
    for i, line in enumerate(file):
        if line[0] == '>':  # If new sequence is found
            record(beginning, i, label, file)  # Add the previous sequence to dataset
            label = line[1:].rstrip()  # Record label of current sequence
            beginning = i + 1  # Record beginning of current sequence
        elif i == len(file) - 1:  # If end of file is reached
            length = record(beginning, i + 1, label, file)

    return length


def record(beginning, end, label, file):
    if label is None:  # First iteration contains no data
        return

    dataset[label] = ""  # So future values can be concatenated
    for line in islice(file, beginning, end, 1):  # Read only lines in sequence
        dataset[label] += line.rstrip()  # Add these lines to the dataset

    length = len(dataset[label])
    return length


if __name__ == "__main__":
    main()
