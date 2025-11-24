# data_profiler.py
# Handles general data profiling tasks

# Import libraries
import numpy as np

class Data_Profiler:

    '''
    count_occurrences(data): count occurrences of array values and store result in 2D array
    data: the numpy array to be counted
    return: a 2D array with unique values and their occurrences
    '''
    def count_occurrences(self, data):
        unique_values, counts = np.unique(data, return_counts=True)
        counted_array = np.vstack((unique_values, counts)).T
        
        return counted_array
    
    '''
    merge_categories(data, cat_data): merges counted data with category data
    data: the original data with counted occurrences
    cat_data: the category data to merge with the amount of occurrences
    return: a 2D array with categories and their occurrences
    '''
    def merge_categories(self, data, cat_data):
        # Create dictionary mapping from data to category
        data_cat_dict = dict(cat_data)
        
        # Map data values to their category
        cat_column = np.array([
            data_cat_dict.get(cat, 'Unknown')
            for cat in data[:, 0] 
        ]).reshape(-1, 1)
        
        # Concatenate category column with counts
        merged_array = np.concatenate(
            (cat_column, data[:, 1].reshape(-1, 1)), 
            axis=1
        )
        
        # Aggregate counts by category
        categories = merged_array[:, 0]
        unique_categories = np.unique(categories)
        
        final_counts = []
        for category in unique_categories:
            # Find indices where the country matches
            indices = np.where(categories == category)

            # Sum the counts for these indices
            total_count = merged_array[indices, 1].astype(int).sum()
            final_counts.append([category, total_count])
            
        return np.array(final_counts)