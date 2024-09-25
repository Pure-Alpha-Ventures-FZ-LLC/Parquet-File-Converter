import os
import pandas as pd

ticker_type = "FOREX" # EQUITY OR FOREX

# Define the directory containing the CSV files (folder ;ocation where the file is existing)
folder_path = 'Data'
output_folder_path = 'processed_data'

# Loop over all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        # Construct the full file path
        csv_file_path = os.path.join(folder_path, filename)
        
        # Load the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Define the Parquet file name by replacing .csv with .parquet
        parquet_file_name = filename.replace('.csv', '.parquet')
        parquet_file_path = os.path.join(output_folder_path, parquet_file_name)
        
        # Save the DataFrame as a Parquet file
        df.to_parquet(parquet_file_path)
        
        if ticker_type == "EQUITY":
            
            # Define the Parquet file name with '_ask'
            filename = filename.split('_')
            filename = filename[0] + '_ask_' + filename[1]
            parquet_ask_file_name = filename.replace('.csv', '.parquet')
            parquet_ask_file_path = os.path.join(output_folder_path, parquet_ask_file_name)
            
            # Save the DataFrame as a Parquet file with '_ask'
            df.to_parquet(parquet_ask_file_path)
            
            print(f"Converted {filename} to {parquet_file_name} and {parquet_ask_file_name}")
        
        else:
            print(f"Converted {filename} to {parquet_file_name}")