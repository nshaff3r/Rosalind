from sys import argv, exit


# Searches for palindromes
def is_palindrome(subsequence, length):
    # Used for iterating
    m = 0
    j = 4
    while True:
        # Finds complimentary sequence
        reverse = ""
        for letter in (map(lambda nucleotide: bases[nucleotide], reversed(subsequence[m:j]))):
            reverse += letter
        # If there's a match, it must be a palindrome
        if subsequence[m:j] == reverse:
            # Writes index and length to file
            outfile.write(f"{i + 1} {j}\n")
        # When there's no palindrome or we've reached the end of the sequence
        if subsequence[m:j] not in compsequence or j > length - 1:
            break
        # Iterate one further through the sequence
        j += 1


# Ensures proper command line arguments
if len(argv) != 3:
    exit("Please use proper command line arguments.")

# Opens output file
outfile = open(argv[2], 'w')

# Reads FASTA file into memory
with open(argv[1], 'r') as file:
    rawsequence = file.readlines()


# Stores formatted sequence
del rawsequence[0]
sequence = ""
for line in rawsequence:
    sequence += line.rstrip()

# Used to reverse DNA sequence
bases = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

# Translates opposite strand of DNA
compsequence = ""
for base in map(lambda nucleotide: bases[nucleotide], reversed(sequence)):
    compsequence += base


# Goes through sequence in chunks of 4, searching for palindromes
for i in range(len(sequence) - 3):
    if sequence[i:i+4] in compsequence:  # If the start of a palindrome is found
        is_palindrome(sequence[i:i+12], len(sequence[i:i+12]))  # Check if it's a palindrome

outfile.close()
