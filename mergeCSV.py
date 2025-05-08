import pandas as pd
import glob
import os

# Set the folder path where the Excel files are located
folder_path = 'DTM/'
output_file = 'DTM.csv'

# Get all Excel file paths in the folder (both .xlsx and .xls)
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx')) + glob.glob(os.path.join(folder_path, '*.xls'))

# Merge all Excel files
dfs = []
for file in excel_files:
    df = pd.read_excel(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

# Save to final merged CSV file
merged_df.to_csv(os.path.join(folder_path, output_file), index=False)

print(f'Merged {len(excel_files)} Excel files into {output_file}')
