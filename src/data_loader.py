import pandas as pd 

def load_data ():
    df_data = pd.read_csv("../data/raw/data.csv")
    df_domains_location = pd.read_csv("../data/raw/domains_location.csv")
    df_traffic = pd.read_csv("../data/raw/traffic.csv")

    return df_data, df_domains_location, df_traffic
