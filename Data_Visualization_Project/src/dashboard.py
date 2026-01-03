import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------ SETTINGS ------------------
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (14, 10)

# ------------------ LOAD DATA ------------------
data = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

data["Order Date"] = pd.to_datetime(data["Order Date"])

# ------------------ KPIs ------------------
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_orders = data["Order ID"].nunique()

# ------------------ AGGREGATIONS ------------------
category_sales = data.groupby("Category")["Sales"].sum()
yearly_sales = data.groupby(data["Order Date"].dt.year)["Sales"].sum()
region_sales = data.groupby("Region")["Sales"].sum()

# ------------------ DASHBOARD LAYOUT ------------------
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 3)

# ------------------ KPI CARDS ------------------
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])

for ax in [ax1, ax2, ax3]:
    ax.axis("off")

ax1.text(0.5, 0.5, f"₹ {total_sales:,.0f}",
         fontsize=20, fontweight="bold", ha="center")
ax1.text(0.5, 0.2, "Total Sales", fontsize=12, ha="center")

ax2.text(0.5, 0.5, f"₹ {total_profit:,.0f}",
         fontsize=20, fontweight="bold", ha="center", color="green")
ax2.text(0.5, 0.2, "Total Profit", fontsize=12, ha="center")

ax3.text(0.5, 0.5, f"{total_orders}",
         fontsize=20, fontweight="bold", ha="center")
ax3.text(0.5, 0.2, "Total Orders", fontsize=12, ha="center")

# ------------------ CATEGORY SALES ------------------
ax4 = fig.add_subplot(gs[1, 0])
category_sales.sort_values().plot(
    kind="barh",
    ax=ax4,
    color="steelblue"
)
ax4.set_title("Sales by Category")
ax4.set_xlabel("Sales")
ax4.set_ylabel("")

# ------------------ YEARLY TREND ------------------
ax5 = fig.add_subplot(gs[1, 1:])
ax5.plot(
    yearly_sales.index,
    yearly_sales.values,
    marker="o",
    linewidth=2
)
ax5.set_title("Yearly Sales Trend")
ax5.set_xlabel("Year")
ax5.set_ylabel("Sales")

# ------------------ REGION PIE ------------------
ax6 = fig.add_subplot(gs[2, 0])
ax6.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=140
)
ax6.set_title("Sales by Region")

# ------------------ HEATMAP ------------------
ax7 = fig.add_subplot(gs[2, 1:])
numeric_data = data.select_dtypes(include="number")

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=ax7
)
ax7.set_title("Correlation Heatmap")

# ------------------ DASHBOARD TITLE ------------------
fig.suptitle(
    "Sales Analytics Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.show()
