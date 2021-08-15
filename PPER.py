from math import factorial

# Takes user input
n = int(input("n: "))
k = int(input("k: "))
# Calculates all partial permutations given the formula n!/(n-r)!
print(int((factorial(n) / factorial(n - k)) % 1000000))
