import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
from datetime import datetime

np.random.seed(42)

# ---- Step 1: Generate synthetic data ----
print("📊 Generating data...")

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
products = ['Software', 'Services', 'Hardware', 'Consulting']
dates = pd.date_range(start="2024-01-01", end="2024-06-30", freq="W")

# Regional sales data
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

# Product category sales
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

print("✅ Data generated.")

# ---- Step 2: Create plots ----
print("📈 Creating charts...")

fig1 = px.line(df_regional, x="Date", y="Sales", color="Region", title="Weekly Sales by Region")
fig2 = px.bar(df_regional.groupby("Region", as_index=False)["Profit"].sum(),
              x="Region", y="Profit", title="Total Profit by Region")
fig3 = px.area(df_category, x="Date", y="Revenue", color="Product", title="Revenue by Product Category")
fig4 = px.pie(df_category.groupby("Product", as_index=False)["Units_Sold"].sum(),
              names="Product", values="Units_Sold", title="Total Units Sold by Product")

# ---- Step 3: Export dashboard HTML ----
print("📝 Writing dashboard HTML...")

dashboard_html = Path("business_dashboard.html")
with open(dashboard_html, "w") as f:
    f.write("<html><head><title>Business Dashboard</title></head><body>\n")
    f.write(f"<h1>Business Dashboard - {datetime.today().strftime('%Y-%m-%d')}</h1>\n")

    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write("<hr>")
    f.write(fig2.to_html(full_html=False, include_plotlyjs=False))
    f.write("<hr>")
    f.write(fig3.to_html(full_html=False, include_plotlyjs=False))
    f.write("<hr>")
    f.write(fig4.to_html(full_html=False, include_plotlyjs=False))

    f.write("</body></html>")

print(f"🎉 Done! Open: {dashboard_html.resolve()}")
