import pandas as pd
from sqlalchemy import create_engine
import yaml

# Load DataFrames into PostgreSQL

def load(customers: pd.DataFrame, products: pd.DataFrame, sales: pd.DataFrame, config_path: str):
    # Load DB config
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    user = config["user"]
    password = config["password"]
    host = config["host"]
    port = config["port"]
    database = config["database"]

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    # Insert data
    customers.to_sql("customers", engine, if_exists="append", index=False)
    products.to_sql("products", engine, if_exists="append", index=False)
    sales.to_sql("sales", engine, if_exists="append", index=False)

    print("Data successfully loaded into PostgreSQL!")