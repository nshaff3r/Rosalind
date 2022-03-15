from Bio import SeqIO

sequences = {}  # Stores DNA sequence
bases = {  # Used to reverse DNA sequence
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}


def main():
    # Parses the input file, storing fasta sequences and ids appropriately
    with open("C:/input.txt", "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            sequences[seq_record.id] = seq_record.seq

    # Writes result to output
    with open("C:/output.txt",'w') as file:
        file.write('\n'.join(correction()))


def correction():
    revdict = {}  # Reversed sequences dict
    for id, sequence in sequences.items():  # Reverses sequence dict to format sequence:[ids]
        revdict.setdefault(sequence, []).append(id)

    for id, sequence in sequences.items():  # Adds ids of matching complimentary sequences
        if reversal(sequence) in revdict:
            revdict[sequence].append(id)

    res = []  # Stores result
    for seq1, ids1 in revdict.items():
        if len(ids1) == 1:  # If the read has no match (there was an error)
            for seq2, ids2 in revdict.items():
                if len(ids2) > 1:  # Correct reads
                    if sum(x != y for x, y in zip(seq1, seq2)) == 1:  # If the hamming distance is 1
                        res.append(f"{seq1}->{seq2}")  # Add both reads to the result
                        break

                    # If the hamming distance to a complimentary read is 1
                    elif sum(x != y for x, y in zip(seq1, reversal(seq2))) == 1:
                        res.append(f"{seq1}->{reversal(seq2)}")  # Add both reads to the result
                        break
    return res


# Returns complimentary sequence
def reversal(seq):
    return ''.join([base for base in map(lambda nucleotide: bases[nucleotide], reversed(seq))])


if __name__ == "__main__":
    main()
