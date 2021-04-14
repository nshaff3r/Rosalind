from sys import argv, exit
import requests
import regex as re

# Checks for proper command line arguments
if len(argv) != 3:
    exit("Please use proper command line arguments")


with open(argv[1], 'r') as infile:
    # Reads input into memory
    dataset = infile.readlines()
    # String to be outputted
    output = ""

    for line in dataset:
        # Removes trailing white space
        line = line.rstrip()
        # Access unique URL and stores its text into fasta
        fasta = requests.get("https://www.uniprot.org/uniprot/" + line + ".fasta").text
        # Separates each line into an item in a list
        sequence = re.split("\n", fasta)
        # Deletes the first line (the ID)
        del sequence[0]
        # Turns sequence back into a string
        sequence = ''.join(sequence)
        # So that access ID is only printed once
        first = True
        # Searches for the N-glycosylation motif in sequence
        for match in re.finditer('[N][^P][S|T][^P]', sequence, overlapped=True):

            if first == True:  # The first iteration
                output += line + '\n'  # Print the access ID
                first = False

            # Adds location to output
            output += str(match.start() + 1) + ' '

        output = output[:-1] + "\n"  # Removes white space at end of line

# Writes output data to file, removing empty lines
with open(argv[2], 'w') as outfile:
    outfile.write(output.strip())
