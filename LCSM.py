from sys import argv
from sys import exit
from Bio import SeqIO
import difflib

# Checks for proper command line arguments
if len(argv) != 3:
    exit("Please use proper command line arguments")

# Opens files
infile = open(argv[1], 'r')
outfile = open(argv[2], 'w')

# Will store FASTA data and ids in a dict and list
sequences = {}
ids = []

# Reads data from fasta file into memory
for seq_record in SeqIO.parse(infile, "fasta"):
    sequences[seq_record.id] = seq_record.seq
    ids.append(seq_record.id)

# Finds matches in first two sequences. This will contain the final motif.
seq1 = sequences[ids[0]]
seq2 = sequences[ids[1]]
masterlist = ""  # Will store all motifs
# Stores the indexes of shared motifs in seq1 and seq2
indexmatch = difflib.SequenceMatcher(None, seq1, seq2, autojunk=False).get_matching_blocks()
# Turns the indexes into string values and adds them to masterlist
for match in indexmatch:
    masterlist += seq1[match[0]:match[0] + match[2]]

""" Compares masterlist to each sequence, updating
the list with conserved motifs each time. A temporary
list is needed because the masterlist must be cleared every iteration
and cannot be cleared before it is indexed"""
for sequence in sequences:
    # Stores shared motifs
    indexmatch = difflib.SequenceMatcher(None, masterlist, sequences[sequence], autojunk=False).get_matching_blocks()
    # Empty list for temporary motif storage
    templist = ""
    # Turns the indexes into string values and adds them to templist
    for match in indexmatch:
        templist += masterlist[match[0]:match[0] + match[2]] + " "
    # Updates (rather than appends to) masterlist
    masterlist = templist

# Sorts motifs by size
indexmatch.sort(key=lambda x: x[2], reverse=True)

# Writes largest shared motif
outfile.write(str(masterlist[indexmatch[0][0]: indexmatch[0][0] + indexmatch[0][2]]))

# Closes files
infile.close()
outfile.close()
