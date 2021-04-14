from sys import argv
from sys import exit
from re import split
from re import findall

if len(argv) != 3:
    exit("Please use proper input")

bases = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}
with open(argv[1], 'r') as file:

    sequence = file.read()
    for base in bases:
        bases[base] = len(findall(base, sequence))


with open(argv[2], 'w') as ofile:

    for key, value in bases.items():
        ofile.write(str(value) + " ")