import csv

# Read transcripts from first file
transcript_map = {}
with open('CSV/Inspira_250_HnB_Batch1_v2 2.csv', newline='', encoding='utf-8') as f1:
    reader = csv.DictReader(f1)
    for row in reader:
        transcript_map[row['Transcript ID']] = row['Transcript']

# Read second file and map transcripts
rows2 = []
with open('CSV/tcx-intents_CXJ-005D_2025-09-25 3.csv', newline='', encoding='utf-8') as f2:
    reader = csv.DictReader(f2)
    for row in reader:
        row['Transcript'] = transcript_map.get(row['Transcript ID'], '')
        rows2.append(row)
    fieldnames2 = reader.fieldnames + ['Transcript']

# Read third file
rows3 = []
with open('CSV/tcx-intent-clusters_CXJ-005D_2025-09-25 3.csv', newline='', encoding='utf-8') as f3:
    reader = csv.DictReader(f3)
    for row in reader:
        rows3.append(row)
    fieldnames3 = reader.fieldnames

# Merge rows2 and rows3 on 'Transcript ID'
merged_rows = []
for row2 in rows2:
    for row3 in rows3:
        if row2['Transcript ID'] == row3['Transcript ID']:
            merged_row = row2.copy()
            for key in row3:
                if key not in merged_row:
                    merged_row[key] = row3[key]
            merged_rows.append(merged_row)
            break

# Write merged output
with open('CSV/final_merged_output.csv', 'w', newline='', encoding='utf-8') as fout:
    fieldnames = list(merged_rows[0].keys())
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(merged_rows)