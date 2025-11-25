# csv_parser.py
# Parse data from a csv file in a useable format like a dataframe

# Import libraries
import pandas as pd
import numpy as np
from numpy import genfromtxt
import warnings

class CSV_Parser:

    '''
    csv_to_chunks(file_path, chunk_size=50000): parses a csv file and yields chunks of data
    file_path: the path to the csv file.
    return: a generator yielding numpy arrays containing the csv data chunks
    '''
    def csv_to_chunks(self, file_path, chunk_size=50000):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            
            csv_chunks = pd.read_csv(
                file_path, 
                delimiter=',', 
                chunksize=chunk_size, 
                header=None,
                on_bad_lines='skip',
                dtype=str
            )
            
            # Generator that returns one chunk at a time as a numpy array
            for chunk in csv_chunks:
                yield chunk.to_numpy()

    '''
    csv_to_array(file_path): parses a csv file into a numpy array
    file_path: the path to the csv file.
    return: a numpy array containing the csv data
    '''
    def csv_to_array(self, file_path):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            
            df = pd.read_csv(
                file_path, 
                delimiter=',', 
                header=None,
                on_bad_lines='skip',
                dtype=str
            )

            return df.to_numpy()
    
    '''
    filter_array(data): Filter strings in numpy array on quotation marks
    data: The numpy array to be filtered (MUST be of string type only!)
    return: A numpy array with filtered strings (without quotation marks)
    '''
    def filter_array(self, data):
        data = data.astype(str)
        filtered_data = np.char.replace(data, '"', '')

        return filtered_data