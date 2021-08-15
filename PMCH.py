from math import factorial
# Opens and reads file, assuming all bases are on one line
with open("c:/input.txt") as file:
    str = file.readlines()[1]

# Finds the number of GC and AU pairs, respectively
gc = str.count("C")
au = str.count("U")

# Calculates the result
print(factorial(gc) * factorial(au))
