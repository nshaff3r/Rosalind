from sys import argv
from sys import exit


# Ensures correct command line input
if len(argv) != 3:
    exit("Please use correct input")

# Reads input into memory
with open(argv[1], 'r') as file:
    sequence = file.read()

# Takes substring from user
sub = input("Substring: ")

# Stores results
locations = []

# Searches for locations of sub in sequence
i = 0
while True:
    test = sequence.find(sub, i)  # Finds initial location
    if test < 0:  # If no more subs are in the sequence
        break
    test += 1  # Program must advance i, and output must be base cased at 1
    locations.append(test)  # Adds location to list for output
    i = test  # Advances iteration

# Prints locations on one line
print(*locations)



