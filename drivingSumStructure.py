import pandas as pd
import numpy as np

txt_file_path = "CFS_Brake_Pedal_Force.txt"

drivingSimText = txt_file_path
csv_file_path = "drivingSimCSV.csv"

# read .txt file into a pandas DataFrame
drivingSimDF = pd.read_csv(txt_file_path, delim_whitespace=True)

# save DataFrame to a .csv file
drivingSimDF.to_csv(csv_file_path, index=True)
print(f"Data successfully written to {csv_file_path}")

print(drivingSimDF.head())  # shows the first few rows of the DataFrame
print(drivingSimDF.info())  # gets an overview of the DataFrame
