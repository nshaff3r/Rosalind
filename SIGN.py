from math import factorial
from itertools import permutations

# Takes input and calculates number of signed permutations
n = int(input("n: "))

# Generates a list of n length for permuting
numbers = [i + 1 for i in range(n)]

# Adds negative versions of each integer in the list
for num in range(1, len(numbers) + 1, 1):
    numbers.append(num * -1)

# Finds all signed permutations, adding them to list perms
perms = []
for num in permutations(numbers, n):
    perms.append(num)

counter = 0
result = ""
# We must not write lists like (1, -1) to our output file
for item in perms:
    absoluteperms = []  # Will store the absolute value of all numbers, to remove duplicates
    for num in item:
        absoluteperms.append(abs(num))
    if len(set(absoluteperms)) == len(absoluteperms):  # Only output non duplicate permutations
        tempresult = ' '.join(map(str, item))
        result += tempresult + '\n'
        counter += 1

with open("c:/output.txt", 'w') as file:
    file.write(str(counter) + '\n' + result)
