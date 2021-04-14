from sys import argv
from sys import exit


def main():

    # Ensures correct command line input
    if len(argv) != 4:
        exit("Please use proper command line arguments.")

    # Stores user input
    dataset = []
    for i in range(1, 4, 1):
        dataset.append(int(argv[i]))

    total = sum(dataset)  # Total alleles

    # Stores frequency of genetic combination, with full being all dominant
    freq = {
        "full": combinations(total - dataset[0], total),
        "most": combinations(0, dataset[1]),
        "half": dataset[1] * dataset[2],
        "none": combinations(0, dataset[2])
    }

    # Probability of each key in freq
    weight = [1, 0.75, 0.5, 0]

    # Calculates total combinations
    combos = combinations(0, total)

    # Weights the frequencies in freq to determine probability
    result = 0
    for i, value in enumerate(freq):
        result += freq[value] * weight[i]

    # Averages and prints result by dividing the amount of combinations
    result /= combos
    print(result)


def combinations(beginning, end):

    customsum = 0

    # Iterates over given range, adding each iteration to the last
    for i in range(beginning, end, 1):
        customsum += i
    return customsum


if __name__ == "__main__":
    main()
