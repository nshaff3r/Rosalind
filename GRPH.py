from sys import argv
from sys import exit
from Bio import SeqIO


# Searches for match between the prefix of a sequence and suffices of other sequences
def match(prefix, entirety):
    for sequence in sequences:  # Searches through all sequences
        # If a match is found from a different sequence
        if prefix == sequences[sequence][-3:] and sequence != entirety:
            outfile.write(sequence + " " + entirety + "\n")  # Write the match to the output file
    return


# Checks for proper command line arguments
if len(argv) != 3:
    exit("Command line must contain input and output arguments.")

# Stores FASTA data
sequences = {}

# Opens input and output files
infile = open(argv[1], 'r')
outfile = open(argv[2], 'w')

# Reads data from fasta file into memory
for seq_record in SeqIO.parse(infile, "fasta"):
    sequences[seq_record.id] = seq_record.seq

# Finds prefix-suffix matches in sequences
for sequence in sequences:
    match(sequences[sequence][:3], sequence)

# Closes files
infile.close()
outfile.close()
