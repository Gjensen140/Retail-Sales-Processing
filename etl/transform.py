import pandas as pd

# Clean and normalize raw DataFrame into customers, products, sales tables
def transform(df: pd.DataFrame):
    
    # Ensure date is parsed
    df['Date'] = pd.to_datetime(df['Date'])

    # Customers table
    customers = df[['Customer ID', 'Gender', 'Age']].drop_duplicates().rename(
        columns={
            "Customer ID": "customer_id",
            "Gender": "gender",
            "Age": "age"
        }
    )

    # Products table
    products = df[['Product Category', 'Price per Unit']].drop_duplicates().rename(
        columns={
            "Product Category": "category",
            "Price per Unit": "price_per_unit"
        }
    ).reset_index(drop=True)
    # Assign product_id (surrogate key)
    products['product_id'] = range(1, len(products) + 1)

    # Map product_id back into sales
    product_map = products.set_index(['category', 'price_per_unit'])['product_id'].to_dict()
    df['product_id'] = df.apply(
        lambda row: product_map[(row['Product Category'], row['Price per Unit'])], axis=1
    )

    # Sales table
    sales = df[['Transaction ID', 'Date', 'Customer ID', 'product_id', 'Quantity', 'Total Amount']].rename(
        columns={
            "Transaction ID": "transaction_id",
            "Date": "date",
            "Customer ID": "customer_id",
            "Quantity": "quantity",
            "Total Amount": "total_amount"
        }
    )

    return customers, products, sales
