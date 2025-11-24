# main.py
# Generate a plot of data from a csv file containing RDW vehicle data

# Import libraries
import sys
import os
from csv_parser import CSV_Parser
from output_generator import Output_Generator
from data_profiler import Data_Profiler

# Constant variables
BASE_DIR = os.path.dirname(__file__)
DATASET = "RDW_dataset.csv"
CATEGORIES = "Car_Manufacturers.csv"
DATASET_PATH = os.path.join(BASE_DIR, "dataset", DATASET)
CATEGORIES_PATH = os.path.join(BASE_DIR, "dataset", CATEGORIES)

def get_results(data, cat_data):
    profiler = Data_Profiler()
    
    counted_brands = profiler.count_occurrences(data)
    counted_countries = profiler.merge_categories(counted_brands, cat_data)

    print(counted_countries)

def get_data():
    parser = CSV_Parser()

    # Load data from csv files
    data = parser.csv_to_array(DATASET_PATH)
    cat_data = parser.csv_to_array(CATEGORIES_PATH)

    # Filter array to remove quotation marks
    data = parser.filter_array(data)
    
    return data, cat_data

def main():
    data, cat_data = get_data()
    get_results(data, cat_data)

main()