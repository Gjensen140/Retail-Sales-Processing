from extract import extract
from transform import transform
from load import load

def main():
    raw_file = "../data/retail_sales_dataset.csv"
    config_file = "../config/db_config.yaml"

    # Extract
    print("Extracting data...")
    df = extract(raw_file)

    # Transform
    print("Transforming data...")
    customers, products, sales = transform(df)

    # Load
    print("Loading data into database...")
    load(customers, products, sales, config_file)

if __name__ == "__main__":
    main()
