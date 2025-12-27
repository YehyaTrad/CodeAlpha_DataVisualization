import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/books_cleaned_data.csv")

##

plt.figure(figsize=(10,5))
sns.histplot(df["Price"], bins=25, color="steelblue")

plt.axvline(df["Price"].mean(), color="red", linestyle="--", label="Average Price")
plt.legend()

plt.title("Most Books Are Priced Around the Average (£)")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()

plt.savefig("visuals/price_distribution.png")
plt.show()

##

stock_counts = df["Stock"].value_counts().reindex([0, 1], fill_value=0)

plt.figure(figsize=(6, 4))
sns.barplot(
    x=["Out of Stock", "In Stock"],
    y=stock_counts.values
)

plt.title("Stock Availability of Books")
plt.ylabel("Number of Books")

plt.savefig("visuals/stock_availability.png")
plt.show()

##

df["Price Range"] = pd.cut(
    df["Price"],
    bins=[0, 20, 40, 60, 100],
    labels=["Low (£0–20)", "Medium (£20–40)", "High (£40–60)", "Very High (£60+)"]
)

price_range_counts = df["Price Range"].value_counts().sort_index()

plt.figure(figsize=(8,5))
sns.barplot(x=price_range_counts.index, y=price_range_counts.values)
plt.title("Books by Price Range")
plt.xlabel("Price Category")
plt.ylabel("Number of Books")

plt.savefig("visuals/price_ranges.png")
plt.show()




