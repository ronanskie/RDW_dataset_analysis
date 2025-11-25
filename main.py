# main.py
# Generate a plot of data from a csv file containing RDW vehicle data

# Import libraries
import os
import numpy as np
from csv_parser import CSV_Parser
from output_generator import Output_Generator
from data_profiler import Data_Profiler

# Constant variables
BASE_DIR = os.path.dirname(__file__)
DATASET = "RDW_dataset_col3.csv"
CATEGORIES = "Car_Manufacturers.csv"
DATASET_PATH = os.path.join(BASE_DIR, "dataset", DATASET)
CATEGORIES_PATH = os.path.join(BASE_DIR, "dataset", CATEGORIES)

'''
aggregate_counts(global_counts, chunk_counts): aggregates counts from chunk into global counts
global_counts: dictionary containing the global counts
chunk_counts: 2D array containing the counts from the current chunk
return: a generator yielding numpy arrays containing the csv data chunks
'''
def aggregate_counts(global_counts, chunk_counts):

    for country, count in chunk_counts:
        count = int(count) 
        global_counts[country] = global_counts.get(country, 0) + count

    return global_counts

'''
get_results(data_generator, cat_data): collects results from data generator and category data
data_generator: generator yielding data chunks from the csv file
cat_data: the category data to merge with the amount of occurrences
return: a 2D array containing the final results
'''
def get_results(data_generator, cat_data):
    profiler = Data_Profiler()
    parser = CSV_Parser()

    global_country_counts = {}
    
    for data in data_generator:
        brand_column = data[:, 0] 
        filtered_brands = parser.filter_array(brand_column)
        counted_brands = profiler.count_occurrences(filtered_brands) 
        counted_countries = profiler.merge_categories(counted_brands, cat_data)
        global_country_counts = aggregate_counts(global_country_counts, counted_countries)

    final_array = np.array(list(global_country_counts.items()))

    return final_array

'''
get_data(): gets the data from the csv datafile
return: a generator yielding chunks of the data and the category data as a numpy array
'''
def get_data():
    parser = CSV_Parser()

    cat_data = parser.csv_to_array(CATEGORIES_PATH)
    cat_data = parser.filter_array(cat_data) 

    data_generator = parser.csv_to_chunks(DATASET_PATH)

    return data_generator, cat_data

'''
main(): Calls the functions needed to parse the data and generate the output
return: Program exits after executing
'''
def main():
    output = Output_Generator()

    data_generator, cat_data = get_data() 
    result = get_results(data_generator, cat_data)

    output.generate_plot(result)
    print(result)

main()