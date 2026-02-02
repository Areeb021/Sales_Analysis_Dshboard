import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page Config (UI)
# ---------------------------
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Performance Dashboard")
st.caption("Sales & Profit analysis using Pandas and Matplotlib")

# ---------------------------
# Data Load (unchanged)
# ---------------------------
df = pd.read_csv("data.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Order_Year"] = df["Order Date"].dt.year
df["Order_Month"] = df["Order Date"].dt.month

# ---------------------------
# KPI SECTION
# ---------------------------
st.subheader("📌 Key Metrics")

k1, k2, k3 = st.columns(3)
k1.metric("Total Sales", f"{df['Sales'].sum():,.0f}")
k2.metric("Total Profit", f"{df['Profit'].sum():,.0f}")
k3.metric("Total Orders", df.shape[0])

st.divider()

# ---------------------------
# CATEGORY ANALYSIS
# ---------------------------
st.header("📦 Category Analysis")

sales_cat = df.groupby("Category")
vz_tot_sales = sales_cat["Sales"].sum()
vz_tot_profit = sales_cat["Profit"].sum()

c1, c2 = st.columns(2)

with c1:
    st.subheader("Sales by Category")
    fig1 = plt.figure()
    plt.bar(vz_tot_sales.index, vz_tot_sales.values)
    plt.xticks(rotation=45)
    plt.title("Total Sales")
    st.pyplot(fig1)
    plt.clf()

with c2:
    st.subheader("Profit by Category")
    fig2 = plt.figure()
    plt.bar(vz_tot_profit.index, vz_tot_profit.values)
    plt.xticks(rotation=45)
    plt.title("Total Profit")
    st.pyplot(fig2)
    plt.clf()

st.divider()

# ---------------------------
# REGION ANALYSIS
# ---------------------------
st.header("🌍 Regional Performance")

region_details = df.groupby("Region")
reg_sales = region_details["Sales"].sum()
reg_profit = region_details["Profit"].sum()

r1, r2 = st.columns(2)

with r1:
    st.subheader("Sales by Region")
    fig3 = plt.figure()
    plt.barh(reg_sales.index, reg_sales.values)
    plt.title("Regional Sales")
    st.pyplot(fig3)
    plt.clf()

with r2:
    st.subheader("Profit by Region")
    fig4 = plt.figure()
    plt.barh(reg_profit.index, reg_profit.values)
    plt.title("Regional Profit")
    st.pyplot(fig4)
    plt.clf()

st.divider()

# ---------------------------
# TIME SERIES
# ---------------------------
st.header("📈 Time-Based Trends")

grp_year = df.groupby("Order_Year")
year_sal = grp_year["Sales"].sum().sort_index()

grp_monthly = df.groupby("Order_Month")
monthly_sale = grp_monthly["Sales"].sum().sort_index()

t1, t2 = st.columns(2)

with t1:
    st.subheader("Yearly Sales Trend")
    fig5 = plt.figure()
    plt.plot(year_sal.index, year_sal.values, marker="o")
    plt.xticks(year_sal.index)
    plt.grid(True)
    st.pyplot(fig5)
    plt.clf()

with t2:
    st.subheader("Monthly Sales Trend")
    fig6 = plt.figure()
    plt.plot(monthly_sale.index, monthly_sale.values, marker="o")
    plt.xticks(monthly_sale.index)
    plt.grid(True)
    st.pyplot(fig6)
    plt.clf()
