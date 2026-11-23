

import numpy as np
import pandas as pd

coffee_name = np.array([
    "Espresso",
    "Latte",
    "Cappuccino",
    "Mocha",
    "Cold Coffee"
])

cups_sold = np.array([120, 95, 150, 80, 110])

price_per_cup = np.array([120, 180, 160, 200, 150])

df = pd.DataFrame({
    "Coffee": coffee_name,
    "Cups Sold": cups_sold,
    "Price (₹)": price_per_cup
})

print("========== COFFEE SHOP SALES DATA ==========")
print(df)

df["Revenue (₹)"] = df["Cups Sold"] * df["Price (₹)"]

print("\n========== UPDATED SALES DATA ==========")
print(df)

most_sold_coffee = df.loc[df["Cups Sold"].idxmax(), "Coffee"]

most_expensive_coffee = df.loc[df["Price (₹)"].idxmax(), "Coffee"]

average_price = df["Price (₹)"].mean()

total_revenue = df["Revenue (₹)"].sum()

print("\n========== FINAL SALES REPORT ==========")
print(f"Most Sold Coffee       : {most_sold_coffee}")
print(f"Most Expensive Coffee  : {most_expensive_coffee}")
print(f"Average Coffee Price   : ₹{average_price:.2f}")
print(f"Total Revenue Earned   : ₹{total_revenue:.2f}")
