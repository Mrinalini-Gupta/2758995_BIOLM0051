Student id: 2758995

Workflow includes:
1. Reformatting split FASTQ files into fasta files and combining all the parts together for each sample 
# Run formated_seq.sh : chmod +x formated_seq.sh
#                       ./formated_seq.sh

2. Blast each sample in NCBI nBLAST and selected 5 reference sequence for each sample.
# Run referenced_seq.sh : chmod +x referenced_seq.sh
#                       ./referenced_seq.sh
This will combine sample A all the parts and reference sequences searched from blast, similarly for the other samples. 

3. All the sample (parts + reference seq) get stored in combined_seq
# Run: cat combined_seq/sample*_blast.fasta > combined_seq/sample_ref_seq.fasta
Sample_ref_seq.fasta in combined_seq stores all the samples parts and reference sequences together ((3*4)+20 = 32 sequences in total)

4. Translating sequences and finding longest orf of each sequences also mentioning which of the 3 forward reading frame it was.
# Run: python combined_seq/translate_orfs.py combined_seq/sample_ref_seq.fasta combined_seq/sample_proteins.fasta 2
Wrote 32 protein sequences

5. Choosing best part of each sample to proceed with MSA
# Run: python combined_seq/pick_best_part.py combined_seq/sample_proteins.fasta combined_seq/improved_for_alignment.fasta
Wrote 24 sequences 4 sample and 20 reference sequence

6. improved_for_alignment.fasta is used for MSA in clustal Omega and phylogenetic tree was achieved for interpretation. 
# Result of alignment in - Aligned_sequences.fasta