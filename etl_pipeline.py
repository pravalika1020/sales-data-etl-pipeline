import pandas as pd

# Extract
df = pd.read_csv("sales_data.csv")

print("Raw Data:")
print(df)

# Transform
df["Revenue"] = df["Quantity"] * df["Price"]

# Remove missing values
df = df.dropna()

# Load
df.to_csv("clean_sales.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nTotal Revenue:", df["Revenue"].sum())

print("\nETL process completed successfully!")