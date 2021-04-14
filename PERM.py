from itertools import permutations

# Generates list with sequence of 1 to user inputted number
numbers = [i + 1 for i in range(int(input("Dataset: ")))]

# Prints and counts permutations
for counter, val in enumerate(permutations(numbers)):
    print(*val)

# Prints the number of permutations
print(counter + 1)
