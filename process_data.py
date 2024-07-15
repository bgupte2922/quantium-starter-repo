import pandas as pd

# File paths for the three CSV files
file_paths = ['C:/Users/Bhagyashree/workspace_python/QuantiumSoftwareEngineeringVirtualInternship/quantium-starter-repo/data/daily_sales_data_0.csv',
              'C:/Users/Bhagyashree/workspace_python/QuantiumSoftwareEngineeringVirtualInternship/quantium-starter-repo/data/daily_sales_data_1.csv',
              'C:/Users/Bhagyashree/workspace_python/QuantiumSoftwareEngineeringVirtualInternship/quantium-starter-repo/data/daily_sales_data_2.csv']

# List to store the dataframes after processing
dfs = []

# Reading each CSV file and filtering rows based on product type
for file_path in file_paths:
    df = pd.read_csv(file_path)
    df = df[df['product'] == 'pink morsel'] # Keep only rows with 'pink morsel'
    df['sales'] = df['quantity'] * df['price'] # Calculate sales
    df = df[['sales', 'date', 'region']] # Select required columns
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Write to output CSV
output_file = 'output.csv'
combined_df.to_csv(output_file, index=False)

print(f"Data processing completed. Output saved to {output_file}")

"""
To run above code:
1. Open a terminal or command prompt.
2. Navigate to the directory where process_data.py is saved using the cd command.
3. Run the script: python process_data.py
4. After the script completes, it will generate an output.csv file containing the processed data
"""