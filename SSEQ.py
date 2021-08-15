from Bio import SeqIO

# Reads and adds sequences to memory
sequences = []
with open("C:/input.txt", "r") as file:
    for seq_record in SeqIO.parse(file, "fasta"):
        sequences.append(seq_record.seq)
s, t = sequences[0], sequences[1]

output = open("C:/output.txt", 'w')

# Searches through string s, updating it's starting index each time a subsequence base is found
previous = 0
for base in t:
    current = s[previous:].index(base)
    current += previous + 1
    output.write(str(current) + ' ')
    previous = current

output.close()
