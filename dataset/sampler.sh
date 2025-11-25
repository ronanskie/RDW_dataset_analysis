#!/bin/bash

# Constant variables
INPUT_FILE="RDW_dataset.csv"
INPUT_FILE_COL3="RDW_dataset_col3.csv"
INPUT_FILE_COL3_UNIQUE="RDW_dataset_col3_unique.csv"
OUTPUT_FILE="RDW_dataset_sample.csv"
SAMPLING_RATE=1000

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file '$INPUT_FILE' not found in the current directory."
    exit 1
fi

echo "Filtering, cutting (col 3), and sorting $INPUT_FILE into '$INPUT_FILE_COL3'..."

# Filter on 'Personenauto' or 'Auto' and extract the 3rd column
awk -F',' '/Personenauto|Auto/ {print $3}' $INPUT_FILE | \
sort > $INPUT_FILE_COL3

# Remove duplicates to get unique values of only brands with more than 1000 occurences
uniq -c $INPUT_FILE_COL3 | \
awk '$1 >= 100 { print $2 }' > "$INPUT_FILE_COL3_UNIQUE"

echo "Filtering and sorting complete."

echo "Sampling '$INPUT_FILE_COL3' (every ${SAMPLING_RATE}th line) into '$OUTPUT_FILE'..."

# Print header and sample every Nth line (default N=1000)
awk -v RATE="$SAMPLING_RATE" 'FNR == 1 || FNR % RATE == 0' "$INPUT_FILE_COL3" > "$OUTPUT_FILE"

echo "Sampled data saved to '$OUTPUT_FILE'."