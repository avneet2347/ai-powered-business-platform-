import pandas as pd

sales = pd.read_csv("data/sales.csv")

sales["revenue"] = sales["quantity"] * sales["price"]

total_revenue = sales["revenue"].sum()

forecast = total_revenue * 1.10

print("Current Revenue:", total_revenue)
print("Next Month Forecast:", forecast)