import sys
import pandas as pd
import string

sys.path.append('../')
from data_loader import load_data

def clean_data():
    # Load data
    df_data, df_domains_location, df_traffic = load_data()

    # Data Cleaning Steps

    # Drop rows with missing values in essential columns for specific tasks
    df_data.dropna(subset=['source_name', 'article_id'], inplace=True)
    df_domains_location['Country'] = df_domains_location['Country'].fillna('UNKNOWN')

    # Drop unnecessary column 'source_id' due to high missing values
    if 'source_id' in df_data.columns:
        df_data.drop(columns=['source_id'], inplace=True)

    # Drop rows with missing values in traffic data if applicable
    if 'GlobalRank' in df_traffic.columns and 'Domain' in df_traffic.columns:
        df_traffic.dropna(subset=['GlobalRank', 'Domain'], inplace=True)

    # Drop rows for specific tasks requiring non-null values in multiple columns
    df_domains_location.dropna(subset=['SourceCommonName', 'Country', 'location'], inplace=True)
    df_data.dropna(subset=['source_name'], inplace=True)
    df_data.dropna(subset=['source_name', 'content'], inplace=True)

    # Impute missing values in non-critical columns with placeholders
    df_data['description'] = df_data['description'].fillna('UNKNOWN')
    df_data.dropna(subset=['title'], inplace=True)
    df_data.dropna(subset=['content'], inplace=True)

    # Drop rows with missing values in essential columns for final tasks
    df_traffic.dropna(subset=['GlobalRank'], inplace=True)
    df_data.dropna(subset=['source_name', 'published_at'], inplace=True)

    # Data Type Consistency Checks

    # Convert 'published_at' in df_data to datetime
    if 'published_at' in df_data.columns:
        df_data['published_at'] = pd.to_datetime(df_data['published_at'], errors='coerce')

    # Convert numerical columns in df_traffic to numeric
    numerical_columns = ['GlobalRank', 'TldRank', 'RefSubNets', 'RefIPs', 'PrevGlobalRank', 'PrevTldRank', 'PrevRefSubNets', 'PrevRefIPs']
    for column in numerical_columns:
        if column in df_traffic.columns:
            df_traffic[column] = pd.to_numeric(df_traffic[column], errors='coerce')

    # Convert categorical columns in df_data to strings
    categorical_columns_data = ['source_name', 'category']
    for column in categorical_columns_data:
        if column in df_data.columns:
            df_data[column] = df_data[column].astype(str)

    # Convert 'Domain' column in df_traffic to string
    if 'Domain' in df_traffic.columns:
        df_traffic['Domain'] = df_traffic['Domain'].astype(str)

    # Convert categorical columns in df_domains_location to strings
    categorical_columns_domains = ['SourceCommonName', 'location', 'Country']
    for column in categorical_columns_domains:
        if column in df_domains_location.columns:
            df_domains_location[column] = df_domains_location[column].astype(str)

    # Normalize and Standardize Steps

    # Helper function to normalize text
    def normalize_text(text):
        if pd.isna(text):
            return text
        # Convert to lowercase, remove punctuation, and strip whitespace
        text = text.lower().strip()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    # Identify columns to normalize and standardize for each DataFrame
    text_columns_data = ['source_name']
    text_columns_domains = ['SourceCommonName', 'location', 'Country']
    text_columns_traffic = ['Domain', 'TLD', 'IDN_Domain', 'IDN_TLD']

    # Normalize text columns in df_data
    for column in text_columns_data:
        if column in df_data.columns:
            df_data[column] = df_data[column].apply(normalize_text)
            print(f"\nUnique values in '{column}' after normalization:\n", df_data[column].unique())

    # Normalize text columns in df_domains_location
    for column in text_columns_domains:
        if column in df_domains_location.columns:
            df_domains_location[column] = df_domains_location[column].apply(normalize_text)
            print(f"\nUnique values in '{column}' after normalization:\n", df_domains_location[column].unique())

    # Normalize text columns in df_traffic
    for column in text_columns_traffic:
        if column in df_traffic.columns:
            df_traffic[column] = df_traffic[column].apply(normalize_text)
            print(f"\nUnique values in '{column}' after normalization:\n", df_traffic[column].unique())

    # Standardize categorical data for countries
    country_standardization = {
        'usa': 'united states',
        'uk': 'united kingdom',
        'india': 'india'
        # Add more mappings as needed
    }

    if 'Country' in df_domains_location.columns:
        df_domains_location['Country'] = df_domains_location['Country'].replace(country_standardization)



    return df_data, df_domains_location, df_traffic

# Run the clean_data function
# df_data, df_domains_location, df_traffic = clean_data()
