# main.py
# Generate a plot of data from a csv file containing RDW vehicle data

# Import libraries
import sys
import os
from csv_parser import CSV_Parser
from output_generator import Output_Generator

# Constant variables
BASE_DIR = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "RDW_dataset_sample.csv")

def get_data():
    parser = CSV_Parser()
    df = parser.csv_to_dataframe(DATASET_PATH)

    print(df.head())

def main():
    get_data()

main()