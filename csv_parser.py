# csv_parser.py
# Parse data from a csv file in a useable format like a dataframe

# Import libraries
import numpy as np
from numpy import genfromtxt
import csv

class CSV_Parser:

    '''
    csv_to_array(file_path): Parse a csv file and return an array
    file_path: The path to the csv file, should be placed in the dataset dir
    return: A numpy array containing the csv data
    '''
    def csv_to_array(self, file_path):
        data = genfromtxt(file_path, delimiter=',', dtype=None)
        return data
    
    '''
    filter_array(data): Filter strings in numpy array on quotation marks
    data: The numpy array to be filtered (MUST be of string type only!)
    return: A numpy array with filtered strings (without quotation marks)
    '''
    def filter_array(self, data):
        filtered_data = np.char.replace(data, '"', '')
        return filtered_data