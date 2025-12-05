import pandas as pd

def clean_data(df):
    # Rename columns to standard names
    df = df.rename(columns={
        "Total Amount": "sales",
        "Date": "date"
    })

    # Convert date column to datetime FIRST
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows where date conversion failed
    df = df.dropna(subset=['date'])

    # Create ML features
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    return df
