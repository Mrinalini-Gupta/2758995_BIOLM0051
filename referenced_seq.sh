mkdir -p combined_seq
echo "Combining sample and ref sequences"
#Combines 3 parts of a sample along with 5 reference sequence from blast 
cat processed/sampleA.fasta sampleA_refs.fasta > combined_seq/sampleA_blast.fasta
cat processed/sampleB.fasta sampleB_refs.fasta > combined_seq/sampleB_blast.fasta
cat processed/sampleC.fasta sampleC_refs.fasta > combined_seq/sampleC_blast.fasta
cat processed/sampleD.fasta sampleD_refs.fasta > combined_seq/sampleD_blast.fasta