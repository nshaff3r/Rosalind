from sys import argv, exit
from textwrap import wrap

# Start codon
start = "ATG"
# Stop codons
stop = ["TAG", "TGA", "TAA"]
# Used to reverse DNA sequence
bases = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}
# Stores codon table
codons = {}
# Stores protein strings
proteins = set()


def main():
    # Ensures proper command line arguments
    if len(argv) != 3:
        exit("Please use proper command line arguments.")

    # Opens and reads codon table (note that "Stop" has been replaced by 'X')
    with open('C:/Users/nshaf/Downloads/codontable.txt', 'r') as file:
        codons = read_codon_table(file.read())

    # Reads FASTA file into memory
    with open(argv[1], 'r') as file:
        rawsequence = file.readlines()

    # Stores formatted sequence
    del rawsequence[0]
    sequence = ""
    for line in rawsequence:
        sequence += line.rstrip()

    # Stores opposite strand of DNA
    compsequence = ""
    for base in map(lambda nucleotide: bases[nucleotide], reversed(sequence)):
        compsequence += base

    # Finds active sequences in DNA and translates them into proteins
    find_active_sequences(sequence, compsequence)

    # Writes protein amino acids to file
    with open(argv[2], 'w') as file:
        for protein in proteins:
            file.write(protein)


# Reads through codon table and stores it in a dict.
def read_codon_table(rawcodons):
    # Temporary string for storing codon info
    strcodons = ""

    # Iterates through codon table (which is filled with whitespace)
    for char in rawcodons:
        if char.isalpha():  # If a character is found
            strcodons += char  # Add that character to the temporary string
            if len(strcodons) == 4:  # If we've iterated over a whole codon and letter
                codons[strcodons[:3]] = strcodons[3]  # Add that codon to dict codons
                strcodons = ""  # Reset our temporary string
    return


# Finds start codons in sequences
def find_active_sequences(sequence, compsequence):
    # Iterates through sequence. Each iteration looks 3 indices ahead.
    for i in range(len(sequence) - 3):
        # If start codon of sequence is found
        if sequence[i] + sequence[i + 1] + sequence[i + 2] == start:
            translate(wrap(sequence[i:], 3))  # Translates from start codon
        # Else if start codon of complimenting sequence is found
        elif compsequence[i] + compsequence[i + 1] + compsequence[i + 2] == start:
            translate(wrap(compsequence[i:], 3))  # Translates from start codon


"""Translates activesequence (which
is a list containing elements of 3
DNA nucleotides) into a protein sequence,
adding the amino acid lettering to set proteins"""


def translate(activesequence):
    protein = ""  # Stores amino acid lettering
    for codon in activesequence:
        if codon in stop:  # If stop codon is reached
            proteins.add(protein + ' \n')  # Add our amino acid lettering to set proteins
            return
        if len(codon) != 3:  # If we've reached the end and there's no stop codon
            return
        protein += codons[codon]  # Add amino acid letter to protein


if __name__ == "__main__":
    main()
