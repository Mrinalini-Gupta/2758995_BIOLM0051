mkdir -p combined_seq
echo "Combining sample and ref sequences"
cat processed/sampleA.fasta sampleA_reference.fasta > combined_seq/sampleA_blast_seq.fasta
cat processed/sampleB.fasta sampleB_reference.fasta > combined_seq/sampleB_blast_seq.fasta
cat processed/sampleC.fasta sampleC_reference.fasta > combined_seq/sampleC_blast_seq.fasta
cat processed/sampleD.fasta sampleD_reference.fasta > combined_seq/sampleD_blast_seq.fasta