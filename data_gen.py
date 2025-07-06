import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# ---- Configuration ----
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
products = ['Software', 'Services', 'Hardware', 'Consulting']

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 30)
dates = pd.date_range(start=start_date, end=end_date, freq='W')

# ---- Generate regional sales data ----
regional_data = []
for date in dates:
    for region in regions:
        sales = np.random.normal(50000, 12000)
        profit = sales * np.random.uniform(0.1, 0.3)
        regional_data.append({
            'Date': date,
            'Region': region,
            'Sales': max(0, round(sales, 2)),
            'Profit': round(profit, 2)
        })

df_regional = pd.DataFrame(regional_data)

# ---- Generate product category sales ----
category_data = []
for date in dates:
    for product in products:
        units_sold = np.random.poisson(lam=200)
        revenue = units_sold * np.random.uniform(200, 800)
        category_data.append({
            'Date': date,
            'Product': product,
            'Units_Sold': units_sold,
            'Revenue': round(revenue, 2)
        })

df_category = pd.DataFrame(category_data)

# ---- Save to CSV ----
df_regional.to_csv("regional_sales_data.csv", index=False)
df_category.to_csv("product_category_sales.csv", index=False)


print("✅ Data generation complete.")
print("Files created: regional_sales_data.csv, product_category_sales.csv")
