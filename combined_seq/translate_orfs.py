from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys
# To check how many arguments were provided when running the script. There should be 4 i.e., script name, input DNA fasta, output protein fasta and translation table (1 or 2)
if len(sys.argv) != 4:
    # If all the argument are not provided it will return the usage message and terminate
    print("Usage: python translate_orfs.py <input_dna_fasta> <output_protein_fasta> <translation_table>")
    print("Example: python find_longest_orfs.py sampleA_dna_all.fasta sampleA_proteins.fasta 2")
    sys.exit(1)
# Take argument from command line
input_fasta = sys.argv[1]
output_fasta = sys.argv[2]
table = int(sys.argv[3])
# List to store output AA SeqRecord objects
aa_sequences = []

# Read all DNA sequences from the input FASTA
sequences = SeqIO.parse(input_fasta, "fasta")
for record in sequences:
    # Stores Nucleotide sequence from the fasta
    dna_seq = record.seq
# Longest orf AA string and which frame 0, 1 or 2 contains it
    best_orf = ""
    best_frame = None
# Translate sequence in all three forward reading frames
    for frame in range(3):
        # Translate starting at this frame; doesn't stops at stop codons (to_stop=False)
        protein = dna_seq[frame:].translate(table=table, to_stop=False)
        # Split translation into fragments separated by stop codons ("*")
        fragments = str(protein).split("*")
        # Stores longest ORF in this frame with its length
        longest_in_frame = max(fragments, key=len)
        # If this ORF is longer than the best one we've seen so far, store it
        if len(longest_in_frame) > len(best_orf):
            best_orf = longest_in_frame
            best_frame = frame
    # Convert the longest ORF string back into a Seq object
    best_protein = Seq(best_orf)
    # To stores fasta header
    desc = record.description
    # Backup if organism name not present
    latin_name = record.id
# checks if fasta contains "organism="
    if "[organism=" in desc:
        start = desc.find("[organism=") + len("[organism=")
        end = desc.find("]", start)
        # Checks if "]" is present
        if end != -1:
            # If not then only extracts organism name replacing spaces by "_"
            latin_name = desc[start:end].replace(" ", "_")
    # Create a new SeqRecord containing the longest ORF for this sequence
    aa_record = SeqRecord(
        best_protein,
        id=record.id,
        name=latin_name,
        description=f"{desc} | longest_ORF_frame={best_frame}",
        annotations={
            "type": "longest ORF",
            # Reading frame from which longest orf came
            "frame": best_frame
        }
    )
# Adds to output list
    aa_sequences.append(aa_record)
    # Saves all translated seq into fasta file
    SeqIO.write(aa_sequences, output_fasta, "fasta")
# Prints how many protein sequences were saved and where
print(f"Wrote {len(aa_sequences)} protein sequences to {output_fasta}")
