from sys import argv, exit


if len(argv) != 2:
    exit("Please use proper command line arguments.")

# Maximum number of RNA strings (for modulo operation).
MAX = 1000000

# Opens and reads codon table (note that "Stop" has been replaced by 'X')
with open('C:/Users/nshaf/Downloads/codontable.txt', 'r') as file:
    rawcodons = file.read()

# Temporary string for storing codon info
strcodons = ""
# Will keep track of amino acid letter frequency.
codons = {}

# Iterates through codon table (which is filled with whitespace)
for char in rawcodons:
    if char.isalpha():  # If a character is found
        strcodons += char  # Add that character to the temporary string
        if len(strcodons) == 4:  # If we've iterated over a whole codon and letter
            if strcodons[3] not in codons:  # And we've never iterated over that letter before
                codons[strcodons[3]] = 0  # Initialize it in the dict
            codons[strcodons[3]] += 1  # Increase the frequency of that letter by one
            strcodons = ""  # Reset our temporary string

# Read the protein string into memory
with open(argv[1], 'r') as file:
    protein = file.read()

# Counts the number of possible mRNA strings
counter = 1

# Iterates through protein sequence
for char in protein:
    counter *= codons[char]  # Multiply mRNA combinations by letter frequency
    if counter >= MAX:  # If counter is greater than 1,000,000
        counter %= MAX  # Reset it back to its remainder

# This accounts for the 3 possible stop codons
counter *= 3

# Prints out the final answer
print(counter % MAX)
