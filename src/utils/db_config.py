import sys
sys.path.append('../')
import pandas as pd
from sqlalchemy import create_engine
from clean_data import clean_data

df_data, df_domains_location, df_traffic = clean_data()

# Define your PostgreSQL database connection parameters
username = 'pgadmin'  # replace with your PostgreSQL username
password = 'pgadmin'  # replace with your PostgreSQL password
database_name = 'newdata'  # replace with your database name
host = 'localhost'  # or your database host
port = '5432'  # default PostgreSQL port

# Create a connection string
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Load the DataFrame into the PostgreSQL database
# Replace 'your_table_name' with the desired name for your table
df_data.to_sql('data', engine, if_exists='replace', index=False)
df_domains_location.to_sql('domains_location', engine, if_exists='replace', index=False)
df_traffic.to_sql('traffic', engine, if_exists='replace', index=False)


print("Data loaded successfully into PostgreSQL!")
