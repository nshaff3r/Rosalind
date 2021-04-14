from sys import argv
from sys import exit


def main():
    if len(argv) != 3:
        exit("Please use proper command line arugments.")

    generations = int(argv[1])

    # The amount of organisms in the last generation
    organisms = 2 ** generations

    # The amount of organisms that can have genotype Aa Bb
    success = organisms - int(argv[2]) + 1

    # The probability that will be outputted
    total = 0

    """ Calculates the probability of success
    (the amount of possible Aa Bb organisms greater
    than argv[2] using the binomial distribution equation."""
    for i in range(organisms - success + 1, success + 1, 1):
        total += binomial_distribution(organisms, i)

    print(total)


# Calculates the factorial of ubound.
def factorial(ubound):
    fact = 1
    for i in range(1, ubound + 1, 1):
        fact *= i
    return fact


# The binomial distribution formula.
def binomial_distribution(n, X):
    numerator = factorial(n) * (0.25 ** X) * 0.75 ** (n - X)
    denominator = factorial(n - X) * factorial(X)
    return numerator / denominator


if __name__ == "__main__":
    main()
