import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression

# 1. Load Data
customers = pd.read_csv("Customer1.csv")
products = pd.read_csv("Product.csv")
sales = pd.read_csv("Sales1.csv")

# Ensure sales date is datetime
if "Date" in sales.columns:
    sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")

# Merge datasets
merged = sales.merge(customers, on="CustomerID").merge(products, on="ProductID")

print("Data successfully merged!\n")

# 2. Customer Segmentation (ICP Profiling)
today = datetime.today()

# Create RFM-style metrics
customer_summary = merged.groupby("CustomerID").agg({
    "SalesAmount": "sum",
    "ProductID": "count",
    "Date": "max"
}).reset_index()

customer_summary.rename(columns={"ProductID": "PurchaseCount", "Date": "LastPurchase"}, inplace=True)

# Add Recency (days since last purchase)
customer_summary["Recency"] = (today - customer_summary["LastPurchase"]).dt.days

# Define segments
def segment_customer(row):
    if row["SalesAmount"] > 5000:
        return "High-Value"
    elif row["PurchaseCount"] > 5:
        return "Frequent Buyer"
    elif row["Recency"] > 180:
        return "Dormant"
    else:
        return "New/Regular"

customer_summary["Segment"] = customer_summary.apply(segment_customer, axis=1)

print("Customer Segmentation Completed!\n")
print(customer_summary.head())

# Export segments
customer_summary.to_csv("Customer_Segments.csv", index=False)
# Top 10 Products
top_products = merged.groupby("ProductName")["SalesAmount"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:\n", top_products)

# Visualization – Top Products
top_products.plot(kind="bar", title="Top 10 Products by Revenue", figsize=(8,5))
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Top_Products.png")
plt.show()

# Monthly Sales Trend
if "Date" in merged.columns:
    merged["Month"] = merged["Date"].dt.to_period("M")
    monthly_sales = merged.groupby("Month")["SalesAmount"].sum()
    monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trends", figsize=(8,5))
    plt.ylabel("Revenue")
    plt.xlabel("Month")
    plt.tight_layout()
    plt.savefig("Monthly_Sales.png")
    plt.show()

segment_counts = customer_summary["Segment"].value_counts()
segment_counts.plot(kind="pie", autopct='%1.1f%%', startangle=90, figsize=(6,6))
plt.title("Customer Segments Distribution")
plt.ylabel("")
plt.savefig("Customer_Segments.png")
plt.show()


def send_campaign(segment, message):
    """
    Simulates a personalized email campaign to customer segments.
    """
    target_customers = customer_summary[customer_summary["Segment"] == segment]
    print(f"\n Sending campaign to {segment} Customers ({len(target_customers)} contacts)...")

    # Mock tracking (randomized)
    opens = np.random.randint(len(target_customers)//2, len(target_customers))
    clicks = np.random.randint(opens//2, opens)
    
    print(f"Message: {message}")
    print(f"Campaign sent! Opens: {opens}, Clicks: {clicks}\n")

    # Export campaign report
    report = pd.DataFrame({
        "Segment": [segment],
        "Total_Customers": [len(target_customers)],
        "Opens": [opens],
        "Clicks": [clicks],
        "Message": [message]
    })
    report.to_csv(f"Campaign_Report_{segment}.csv", index=False, mode='w')

# Example Campaigns
send_campaign("High-Value", "Exclusive offer: 25% off on premium products!")
send_campaign("Frequent Buyer", "Special reward: Free delivery on your next order!")
send_campaign("Dormant", "We miss you! Come back & enjoy 15% off.")
send_campaign("New/Regular", "Welcome! Flat 10% off on your first purchase.")

# 5. Predictive Sales Forecast
if "Date" in merged.columns:
    merged["Month_Num"] = merged["Date"].dt.month
    monthly_grouped = merged.groupby("Month_Num")["SalesAmount"].sum().reset_index()

    X = monthly_grouped[["Month_Num"]]
    y = monthly_grouped["SalesAmount"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict next month's sales
    next_month = [[max(X["Month_Num"]) + 1]]
    forecast = model.predict(next_month)
    print(f"\n Forecasted Sales for Next Month: {forecast[0]:.2f}")


            

