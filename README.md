Student id: 2758995
1. Project Overview:


This project analyses four unknown meat samples provided as split FASTQ files.
The goal is to identify their species of origin using DNA barcoding and phylogenetic reconstruction. Workflow includes:
- Reformatting split FASTQ files into fasta files and combining all the parts together for each sample.

- Blast each sample in NCBI nBLAST and selected 5 reference sequence for each sample.

- All the sample (parts + reference seq) get stored in combined_seq.

- Translating sequences and finding longest orf of each sequences also mentioning which of the 3 forward reading frame it was.

- Choosing best part of each sample to proceed with MSA.

- MSA in clustal Omega and phylogenetic tree was achieved for interpretation. 
 Result of alignment in - Aligned_sequences.fasta

 2. Key Features

-Shell script to automatically merge split FASTQ files.
-Python ORF finder using BioPython.
-Automated translation of sequences in all three reading frames.

3. Repository Structure:
Project root/
|
|--combined_seq/        
|      |--improved_for_alignment.fasta   #fasta file used for MSA containing 4 unknown sample 
|      |                                   + 20 reference sequence
|      |--pick_best_part.py              #Python script to choose part of sample that
|      |                                 contains max number of AA
|      |--sample_proteins.fasta          #fasta file containing translated sequences
|      |--sample_ref_seq.fasta      #Combined fasta file containing 
|      |                             all the samples + reference sequences
|      |--sampleA_blast.fasta       #fasta file containing all the parts of 
|      |--sampleB_blast.fasta       sample along with reference sequences    
|      |--sampleC_blast.fasta
|      |--sampleD_blast.fasta
|      |--translate_orfs.py              #Python script to translate and find longest ORFs 
|--fasta_parts              #Converted fasta files of all parts of samples
|      |--SampleA_part1.fasta
|      |--SampleA_part2.fasta
|      |--        .
|      |--SampleD_part3.fasta
|--processed                 #Merged fasta files for each sample
|      |--SampleA.fasta
|      |--        .
|      |--SampleD.fasta
|
|--Aligned_sequences.fa       #Contains result of Clustal Omega MSA
|--formated_seq.sh            #Shell script to change FASTQ-->fasta and merge split seq
|--README                        
|--referenced_seq.sh          #Combines unknown sample sequence with their reference sequence
|--samples.txt                   #Text file contains sample names for while loop iterations
|--sampleA_part1.FASTQ           #Original FASTQ files for all the samples
|--sampleA_part2.FASTQ
|--sampleA_part3.FASTQ
|--sampleA_refs.fasta          #Reference sequences from nBLAST for each sample 
|--   .
|--   .
|--sampleD.refs.fasta


4. Installation and Usage Instruction

4.1 Required software: BioPython
pip install biopython
Bash shell
Git
Python
 
4.2 Reproducing Analysis:

 Step 1.
chmod +x formated_seq.sh
/formated_seq.sh

FASTQ->fasta and merge split fasta files

Step 2.
 chmod +x referenced_seq.sh
./referenced_seq.sh

Combines sample sequence and reference sequence

Step 3. 
cat combined_seq/sample*_blast.fasta > combined_seq/sample_ref_seq.fasta

Sample_ref_seq.fasta in combined_seq stores all the samples parts and reference sequences together ((3*4)+20 = 32 sequences in total).

Step 4.
python combined_seq/translate_orfs.py combined_seq/sample_ref_seq.fasta combined_seq/sample_proteins.fasta 2

Translate and extracts longest ORFs (Wrote 32 protein sequences).

Step 5.
python combined_seq/pick_best_part.py combined_seq/sample_proteins.fasta combined_seq/improved_for_alignment.fasta

Wrote 24 sequences 4 sample and 20 reference sequence.

Step 6.
improved_for_alignment.fasta is used for MSA
Aligned_sequences.fa contains result of MSA.
