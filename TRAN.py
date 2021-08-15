from Bio import SeqIO

# Reads and adds sequences to memory
sequences = []
with open("C:/input.txt", "r") as file:
    for seq_record in SeqIO.parse(file, "fasta"):
        sequences.append(seq_record.seq)
s1, s2 = sequences[0], sequences[1]

# These are the transition point mutations
pairings = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

# Keeps track of the amount of transitions and transvertions found
transitions = 0
transversions = 0

# Goes base by base in each string, comparing
# each value and checking for point mutation
for x, y in zip(s1, s2):
    if x != y:
        if pairings[x] != y:
            transversions += 1
        else:
            transitions += 1

print(transitions/transversions)
