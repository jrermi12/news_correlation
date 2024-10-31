import pandas as pd 

def load_data ():
    df_data = pd.read_csv("/home/jrermi/Documents/1 GITHUB/10_Academy/SELF/WEEK 0/news_correlation/data/raw/data.csv")
    df_domains_location = pd.read_csv("/home/jrermi/Documents/1 GITHUB/10_Academy/SELF/WEEK 0/news_correlation/data/raw/domains_location.csv")
    df_traffic = pd.read_csv("/home/jrermi/Documents/1 GITHUB/10_Academy/SELF/WEEK 0/news_correlation/data/raw/traffic.csv")

    # df_data = pd.read_csv("../data/raw/data.csv")
    # df_domains_location = pd.read_csv("../data/raw/domains_location.csv")
    # df_traffic = pd.read_csv("../data/raw/traffic.csv")

    return df_data, df_domains_location, df_traffic
