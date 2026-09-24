# Sales Data ETL Pipeline

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and Pandas.

The pipeline reads raw sales data from a CSV file, cleans and transforms the data, calculates revenue, and creates a processed CSV file.

## Technologies Used

- Python
- Pandas
- CSV
- Git & GitHub

## ETL Process

### 1. Extract

The pipeline reads raw sales data from `sales_data.csv`.

### 2. Transform

The data is transformed by:

- Calculating revenue using Quantity × Price
- Removing missing values
- Processing the sales data using Pandas

### 3. Load

The transformed data is saved into `clean_sales.csv`.

## Project Structure

```text
sales-data-etl-pipeline/
│
├── sales_data.csv
├── clean_sales.csv
├── etl_pipeline.py
└── README.md