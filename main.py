# main.py
# Generate a plot of data from a csv file containing RDW vehicle data

# Import libraries
import sys
import os
from csv_parser import CSV_Parser
from output_generator import Output_Generator

# Constant variables
BASE_DIR = os.path.dirname(__file__)
DATASET = "RDW_dataset_sample.csv"
DATASET_PATH = os.path.join(BASE_DIR, "dataset", DATASET)

def get_data():
    parser = CSV_Parser()
    data = parser.csv_to_array(DATASET_PATH)
    data = parser.filter_array(data)
    print(data)

def main():
    get_data()

main()