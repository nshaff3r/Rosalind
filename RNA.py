from sys import argv
from sys import exit
from re import split
from re import findall

if len(argv) != 3:
    exit("Please use proper input")

with open(argv[1], 'r') as file:

    sequence = file.read()

with open(argv[2], 'w') as ofile:

    ofile.write(sequence.replace('T', 'U'))
