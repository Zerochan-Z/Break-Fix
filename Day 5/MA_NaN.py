import pandas as pd
import os 

file_name = "market_data.csv"
if not os.path.exists(file_name):
    print(f"{file_name} not found. Please make sure the file is in the current directory.")
else:
    df = pd.read_csv("market_data.csv")
    print(df.head())