from sys import argv, exit

# Ensures proper command line arguments
if len(argv) != 2:
    exit("Please use proper command line arguments.")

# Dict to store masses
masses = {}

# Will store weighted string
weight = 0

# Reads and formats monoisotopic mass table into memory
with open("C:/Users/nshaf/Downloads/Monoisotopic.txt", 'r') as file:
    for line in file.readlines():
        masses[line[0]] = float(line[1:].replace(' ', '').rstrip())

# Reads protein sequence into memory
with open(argv[1], 'r') as file:
    protein = file.read()

# Adds the weight of each amino acid in protein
for letter in protein:
    weight += masses[letter]

print(weight)
