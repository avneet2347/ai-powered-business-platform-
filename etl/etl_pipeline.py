import pandas as pd

sales = pd.read_csv("data/sales.csv")

sales.drop_duplicates(inplace=True)

sales.fillna(0, inplace=True)

sales["revenue"] = sales["quantity"] * sales["price"]

sales.to_csv("data/clean_sales.csv", index=False)

print("ETL Pipeline Executed Successfully")