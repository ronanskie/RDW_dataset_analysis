# csv_parser.py
# Parse data from a csv file in a useable format like a dataframe

# Import libraries
import pandas as pd
import csv

class CSV_Parser:

    '''
    csv_to_dataframe(file_path): Parse a csv file and return a dataframe
    file_path: The path to the csv file, should be placed in the dataset dir
    return: A pandas dataframe containing the csv data
    '''
    def csv_to_dataframe(self, file_path):
        df = pd.read_csv(file_path)
        return df