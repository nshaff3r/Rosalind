from sys import argv
from sys import exit


# Checks for proper command line usage
length = len(argv)
if length != 7:
    exit("Please use proper command line arguments.")

# Number of offspring out of 2 with dominate phenotype
weights = [2, 2, 2, 1.5, 1, 0]
output = 0

# Multiplies input with probabilities
for i in range(length - 1):
    output += weights[i] * int(argv[i + 1])

print(output)
