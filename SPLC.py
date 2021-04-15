from Bio import SeqIO
from textwrap import wrap

# Opens FASTA file and removes introns from main DNA sequence
with open("C:/input.txt", 'r') as file:
    first = True
    for seq_record in SeqIO.parse(file, "fasta"):
        if first == True:
            main = str(seq_record.seq)
            first = False
        else:
            main = main.replace(str(seq_record.seq), '')

# Opens and reads codon table into memory. Note that the stop codon has been replaced by 'X'.
with open("C:/DNA.txt", 'r') as file:
    rawcodons = file.read()
    # Dict storing DNA bases and the amino acids they code for
    codons = {}
    # Temporary string for storing codon info
    temp = ""
    # Iterates through codon table (which is filled with whitespace)
    for char in rawcodons:
        if char.isalpha():  # If a character is found
            temp += char  # Add that character to the temporary string
            if len(temp) == 4:  # If we've iterated over a whole codon and letter
                codons[temp[:3]] = temp[3]  # Add that codon to dict codons
                temp = ""  # Reset our temporary string

# Divides DNA nucleotides into groups of 3 to be translated to proteins
main = wrap(main, 3)
# Stores protein amino acids
protein = ""
# Converts DNA nucleotides into amino acids using the codon table
for base in map(lambda nucleotide: codons[nucleotide], main):
    protein += base

# Writes the final protein string to file
with open ("C:/output.txt", 'w') as file:
    file.write(protein[:-1] + "\n")
