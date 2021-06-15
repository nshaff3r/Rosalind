from Bio import SeqIO
from random import choice

# Will store match and sequence information
leftmatches = []
rightmatches = []
sequences = {}


def main():
    # Will store names of all sequence fasta ids
    ids = []
    # Parses the input file, storing fasta sequences and ids appropriately
    with open("C:/input.txt", "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            sequences[seq_record.id] = seq_record.seq
            ids.append(seq_record.id)
    outfile = open("C:/output.txt", "w")

    # Sets a equal to a random sequence
    a = sequences[choice(ids)]
    # Used for the corner case that a equals the right most sequence in the sorted string
    rightmost = True
    # Iterates through all sequences, comparing each sequence, b, to a
    for sequence in sequences:
        b = sequences[sequence]
        # Since not all sequences are the same length,
        # we must use the higher of the two so we don't miss anything
        higher = max(len(a), len(b))
        # All matches are guaranteed to be longer
        # than half the length of the highest string
        for index in range(int(higher / 2), higher, 1):
            # If the ending of a equals the beginning of b
            if a[-index:] == b[:index]:
                # We must be somewhere in the middle of the sorted string,
                # so we can start searching for all matches to the left
                left(a)
                # Once we've searched for and found all matches to the left,
                # we should add out center match to the sorted string
                leftmatches.append(str(a))
                rightmatches.append(str(b[index:]))
                # Now we must search for all matches to the right
                right(b)
                # At this point, we've found all matches and we can write
                # them to our output file
                for match in leftmatches:
                    outfile.write(match)
                for match in rightmatches:
                    outfile.write(match)
                # Since something matched the ending of a, then a must not
                # be the rightmost string.
                rightmost = False

    # The corner case that a was the rightmost string
    if rightmost:
        # Find all matches to the left of a
        left(a)
        # Add a to our sorted sequence
        leftmatches.append(a)
        # Write the sequence to file
        for match in leftmatches:
            outfile.write(str(match))


def left(start):
    global leftmatches
    a = start
    # Will keep track of the highest match
    highest = [0, ""]
    for sequence in sequences:
        b = sequences[sequence]
        higher = max(len(a), len(b))
        for index in range(int(higher / 2), higher, 1):
            if a[:index] == b[-index:]:
                # If it's the largest overlap of any match, update highest
                if index > highest[0]:
                    highest = [index, b]
    # If a match was found (highest was updated)
    if highest[0] > 0:
        # Add that match to the beginning of left matches
        leftmatches = [str((highest[1][:len(highest[1]) - highest[0]]))] + leftmatches
        # Search for matches to the left of that match
        left(highest[1])


def right(start):
    a = start
    highest = [0, ""]
    for sequence in sequences:
        b = sequences[sequence]
        higher = max(len(a), len(b))
        for index in range(int(higher / 2), higher, 1):
            if a[-index:] == b[:index]:
                if index > highest[0]:
                    highest = [index, b]
    if highest[0] > 0:
        # Add that match to the end of right matches
        rightmatches.append(str(highest[1][highest[0]:]))
        # Search for matches to the right of that match
        right(highest[1])


if __name__ == "__main__":
    main()
