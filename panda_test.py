import pandas as pd
import numpy as np
# Replace 'your_file.csv' with the path to your CSV file
file_path = 'AIR_EMISSIONS_06122023151445542.csv'
list=np.linspace(0,19,20, dtype=int)
print(list)
list=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
columns_to_extract_indices = [1,3,7,14]

# Open the CSV file
with open(file_path, 'r') as csv_file:
    # Read all lines from the CSV file
    lines = csv_file.readlines()
    # Extract only the specified columns
    extracted_data = []
    for line in lines:
        # Split the line into columns
        columns = line.strip().split(',')

        # Select the specified columns
        selected_columns = [columns[i] for i in columns_to_extract_indices]

        # Append the selected columns to the result
        extracted_data.append(selected_columns)

# Display the resulting list of lists
print(extracted_data[1:20])
