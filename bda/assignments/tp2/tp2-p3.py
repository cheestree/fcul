import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text

# Load CSV
df = pd.read_csv("../dias_catalogue.csv")

# clean the dataset
df = df.replace('', None)
df.replace([np.inf, -np.inf], np.nan, inplace=True)


# Create a connection to MySQL
# Replace user, password, host, port, database_name with your info
#engine = create_engine("mysql+mysqlconnector://user:password@host:port/database_name")
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/")
# Execute raw SQL to create database
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS astro_database"))
    conn.commit()
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/astro_database")