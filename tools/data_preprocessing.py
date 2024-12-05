import pandas as pd
import numpy as np

def load_data(file_path):
    """Load dataset from a file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None

def clean_data(data):
    """Clean dataset by handling missing values and removing duplicates."""
    data = data.drop_duplicates()
    data = data.ffill()  # Forward fill missing values
    print("Data cleaned successfully.")
    return data

def normalize_data(data, columns):
    """Normalize specific columns of the dataset."""
    for col in columns:
        if col in data.columns:
            data[col] = (data[col] - data[col].mean()) / data[col].std()
    print("Data normalized successfully.")
    return data

if __name__ == "__main__":
    file_path = "data/sensor_data.csv"
    data = load_data(file_path)
    if data is not None:
        data = clean_data(data)
        data = normalize_data(data, ["temperature", "pressure"])
        print(data.head())

