from sys import argv
from sys import exit
from textwrap import wrap


def main():

    # Ensures proper command line arguments
    if len(argv) != 4:
        exit("Please use proper input")

    # Reads table into memory
    with open(argv[1], 'r') as file:
        rawcodons = file.read()

    # Other data structures for table, with dict being the final
    strcodons = ""
    codons = {}

    # Removes spaces from rawcodons and stores it in strcodons
    for element in rawcodons:
        for value in element:
            if value != ' ':
                strcodons += value.rstrip()

    # Separates strcodons into list with elements of 4 characters
    listcodons = wrap(strcodons, 4)

    # Stores codons and their letters in dict
    for i in range(len(listcodons)):
        codon = listcodons[i][:3]
        letter = listcodons[i][3]
        codons[codon] = letter

    # Opens and reads RNA string
    with open(argv[2], 'r') as file:
        dataset = file.read()
    dataset = wrap(dataset, 3)

    # Translates to protein based off codons dict
    protein = ""
    for i in range(len(dataset)):
        if dataset[i] in codons:
            protein += codons[dataset[i]]

    # Removes stop codon, which is labeled as X rather than "Stop"
    protein = protein.replace('X', '')

    # Writes protein to output file
    with open(argv[3], 'w') as file:
        file.write(protein)


if __name__ == "__main__":
    main()
