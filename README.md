# Retail Sales Data Warehouse

A portfolio project that demonstrates how to build a **mini data warehouse** for retail sales using **SQL, Python (Pandas), and PostgreSQL**.  
The project includes a simple **ETL pipeline**, a normalized schema, and analytical queries to uncover business insights.

## 🗄️ Data Model

The dataset includes columns: `Transaction ID`, `Date`, `Customer ID`, `Gender`, `Age`, `Product Category`, `Quantity`, `Price per Unit`, `Total Amount`.  

It was normalized into three tables:

- **customers**
  - `customer_id` (PK)  
  - `gender`  
  - `age`  

- **products**
  - `product_id` (PK, surrogate)  
  - `category`  
  - `price_per_unit`  

- **sales**
  - `transaction_id` (PK)  
  - `date`  
  - `customer_id` (FK → customers)  
  - `product_id` (FK → products)  
  - `quantity`  
  - `total_amount`

 ## ⚙️ ETL Workflow

1. **Extract** → Read raw CSV into Pandas.  
2. **Transform** →  
   - Normalize into `customers`, `products`, `sales`.  
   - Assign surrogate keys.  
   - Parse dates + clean columns.  
3. **Load** → Insert into PostgreSQL with SQLAlchemy.  

Data Pipeline:  
- `extract.py` → reads CSV  
- `transform.py` → cleans + normalizes  
- `load.py` → inserts into Postgres  
- `run_etl.py` → orchestrates the steps

