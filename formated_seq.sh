#!/bin/bash
mkdir -p processed
mkdir -p fasta_parts
# Runs 4 time for each sample
while read SAMPLE; do
echo "Processing $SAMPLE ..."
# Runs 3 times coverting all th parts of sample from FASTQ to fasta 
for x in 1 2 3; do
INPUT="${SAMPLE}_part${x}.FASTQ"
OUTPUT="fasta_parts/${SAMPLE}_part${x}.fasta"
# Takes header and sequence line from FASTQ and gives output
awk 'NR%4==1{print ">"substr($0,2)} NR%4==2{print}' "$INPUT" > "$OUTPUT"
done
#Combines all the 3 parts of sample in fasta
cat fasta_parts/${SAMPLE}_part1.fasta fasta_parts/${SAMPLE}_part2.fasta fasta_parts/${SAMPLE}_part3.fasta > processed/${SAMPLE}.fasta
echo "Created/${SAMPLE}.fasta"
echo
done < samples.txt
#samples.txt stores name of the 4 sample so that while loop runs 4 times
echo "All sample done"
