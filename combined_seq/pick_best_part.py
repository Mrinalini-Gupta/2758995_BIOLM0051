from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys
if len(sys.argv) != 3:
    print("Usage: python pick_best_parts.py <input_orf_fasta> <output_fasta>")
    sys.exit(1)
input_fasta = sys.argv[1]
output_fasta = sys.argv[2]
# Define which IDs belong to each sample
sample_groups = {
    "SampleA": ["sampleA_part_1", "sampleA_part_2", "sampleA_part_3"],
    "SampleB": ["sampleB_part1", "sampleB_part2", "sampleB_part3"],
    "SampleC": ["sampleC_part1", "sampleC_part2", "sampleC_part3"],
    "SampleD": ["sampleD_part1", "sampleD_part2", "sampleD_part3"],
}
# Read all records
records = list(SeqIO.parse(input_fasta, "fasta"))
id_to_record = {rec.id: rec for rec in records}

output_records = []

# For each sample, choose the "best" part = longest protein sequence
for sample_name, part_ids in sample_groups.items():
    best_rec = None
    best_len = -1
    for pid in part_ids:
        if pid not in id_to_record:
            continue
        rec = id_to_record[pid]
        length = len(rec.seq)
        if length > best_len:
            best_len = length
            best_rec = rec
    if best_rec is None:
        print(
            f"WARNING: no parts found for {sample_name}, skipping this sample.")
        continue
    best_sample_rec = SeqRecord(
        best_rec.seq,
        id=sample_name,
        description=f"best part ({best_rec.id}), length={best_len} aa"
    )
    output_records.append(best_sample_rec)
    print(f"{sample_name}: selected {best_rec.id} (length {best_len} aa) as best part.")
# Checks if ID is one of the sample parts


def is_sample_part(rec_id: str) -> bool:
    for part_list in sample_groups.values():
        if rec_id in part_list:
            return True
    return False


# Add all reference sequences unchanged
for rec in records:
    if not is_sample_part(rec.id):
        output_records.append(rec)
# Write new FASTA
SeqIO.write(output_records, output_fasta, "fasta")
print(f"Wrote {len(output_records)} sequences to {output_fasta}")
