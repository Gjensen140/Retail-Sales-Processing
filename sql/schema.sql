DROP TABLE IF EXISTS sales CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS products CASCADE;

-- Customers table
CREATE TABLE customers (
    customer_id VARCHAR PRIMARY KEY,
    gender VARCHAR(10),
    age INT
);

-- Products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category VARCHAR(100),
    price_per_unit NUMERIC
);

-- Sales table
CREATE TABLE sales (
    transaction_id INT PRIMARY KEY,
    date DATE,
    customer_id VARCHAR REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    total_amount NUMERIC
);
