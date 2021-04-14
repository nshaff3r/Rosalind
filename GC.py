from sys import argv
from sys import exit
from itertools import islice
from re import findall

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
    read(data)

    # Keeps track of highest GC count
    hfreq = 0
    hseq = ""

    # Counts amount of GC bases per sequence and records highest
    for sequence in dataset:
        freq = len(findall(r'[G C]', dataset[sequence]))
        freq = freq * 100 / len(dataset[sequence])
        if freq > hfreq:
            hfreq = freq
            hseq = sequence

    # Formats highest sequence for writing
    result = hseq + "\n" + str(hfreq) + "%"

    # Writes highest sequence to file
    with open(argv[2], 'w') as file:
        file.writelines(result)


def read(file):

    beginning = 0
    label = None  # For first iteration
    for i, line in enumerate(file):
        if line[0] == '>':  # If new sequence is found
            record(beginning, i, label, file)  # Add the previous sequence to dataset
            label = line[1:].rstrip()  # Record label of current sequence
            beginning = i + 1  # Record beginning of current sequence
        elif i == len(file) - 1:  # If end of file is reached
            record(beginning, i + 1, label, file)

    return


def record(beginning, end, label, file):

    if label is None:  # First iteration contains no data
        return

    dataset[label] = ""  # So future values can be concatenated
    for line in islice(file, beginning, end, 1):  # Read only lines in sequence
        dataset[label] += line.rstrip()  # Add these lines to the dataset

    return


if __name__ == "__main__":
    main()
