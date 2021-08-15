from re import split, findall
from math import log10

with open("c:/input.txt", "r") as file:
    reader = file.readlines()

output = open("c:/output.txt", 'w')

# Adds DNA string
string = reader[0]

# Creates array of GC probabilitye
arr = split(' ', reader[1])

# Counts the number of GC and AT bases in the string
gc = len(findall("G|C", string))
at = len(findall("A|T", string))

for i in range(len(arr)):
    arr[i] = float(arr[i])
    # Calculates the probability of random strings
    # matching using the common log as inflation
    output.write(str(round(log10(pow(arr[i] / 2, gc)) + log10(pow((1 - arr[i])/2, at)), 3)) + ' ')
