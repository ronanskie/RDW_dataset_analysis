# csv_parser.py
# Parse data from a csv file in a useable format like a dataframe

# Import libraries
import pandas as pd
import numpy as np
from numpy import genfromtxt
import warnings

class CSV_Parser:

    '''
    csv_to_array(file_path): parse a csv file and return an array
    file_path: the path to the csv file, should be placed in the dataset dir
    return: a numpy array containing the csv data
    '''
    def csv_to_array(self, file_path):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)

            data = genfromtxt(
                file_path,
                delimiter=',',
                dtype=None, 
                invalid_raise=False
            )
        return data
    
    '''
    filter_array(data): Filter strings in numpy array on quotation marks
    data: The numpy array to be filtered (MUST be of string type only!)
    return: A numpy array with filtered strings (without quotation marks)
    '''
    def filter_array(self, data):
        filtered_data = np.char.replace(data, '"', '')
        return filtered_data