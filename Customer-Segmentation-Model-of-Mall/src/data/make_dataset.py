import pandas as pd

def load_data(data_path):
    df = pd.read_csv(data_path)
    
    print("Printing first 10 rows:")
    print(df.head())
    print("Shape of data is:",df.shape)
    print("data types of dataset:")
    print(df.dtypes)
    print("Descriptive statistics:")
    print(df.describe())
    return df