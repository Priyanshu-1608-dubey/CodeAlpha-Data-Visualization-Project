import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Style settings
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Create output directory
os.makedirs("output/charts", exist_ok=True)

# Load dataset (encoding fixed)
data = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# ------------------ Bar Chart ------------------
plt.figure()
category_sales = data.groupby("Category")["Sales"].sum().sort_values()
category_sales.plot(kind="barh", color="steelblue")
plt.title("Total Sales by Product Category", fontsize=14, fontweight="bold")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("output/charts/sales_by_category.png", dpi=300)
plt.show()

# ------------------ Line Chart ------------------
data["Order Date"] = pd.to_datetime(data["Order Date"])
yearly_sales = data.groupby(data["Order Date"].dt.year)["Sales"].sum()

plt.figure()
plt.plot(
    yearly_sales.index,
    yearly_sales.values,
    marker="o",
    linestyle="-",
    linewidth=2
)
plt.title("Yearly Sales Trend", fontsize=14, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("output/charts/yearly_sales_trend.png", dpi=300)
plt.show()

# ------------------ Pie Chart ------------------
plt.figure()
region_sales = data.groupby("Region")["Sales"].sum()

plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Sales Distribution by Region", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("output/charts/sales_by_region.png", dpi=300)
plt.show()

# ------------------ Heatmap ------------------
plt.figure(figsize=(8, 6))
numeric_data = data.select_dtypes(include="number")

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
plt.title("Correlation Heatmap of Numerical Features", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("output/charts/correlation_heatmap.png", dpi=300)
plt.show()
