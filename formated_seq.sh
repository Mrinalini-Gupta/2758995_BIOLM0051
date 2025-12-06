#!/bin/bash
mkdir -p processed
mkdir -p fasta_parts
while read SAMPLE; do
echo "Processing $SAMPLE ..."
for x in 1 2 3; do
INPUT="${SAMPLE}_part${x}.FASTQ"
OUTPUT="fasta_parts/${SAMPLE}_part${x}.fasta"
awk 'NR%4==1{print ">"substr($0,2)} NR%4==2{print}' "$INPUT" > "$OUTPUT"
done

cat fasta_parts/${SAMPLE}_part1.fasta fasta_parts/${SAMPLE}_part2.fasta fasta_parts/${SAMPLE}_part3.fasta > processed/${SAMPLE}.fasta
echo "Created processed/${SAMPLE}.fasta"
echo
done < samples.txt
echo "All sample done"
