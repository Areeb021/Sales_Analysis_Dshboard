import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Sales Analysis Dashboard")
st.caption("Basic analysis using Pandas & Matplotlib")

# ---------------------------
# File Upload
# ---------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    # ---------------------------
    # Date Processing (same logic)
    # ---------------------------
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Order_Year"] = df["Order Date"].dt.year
    df["Order_Month"] = df["Order Date"].dt.month

    # ---------------------------
    # Group by Category
    # ---------------------------
    st.subheader("📦 Category-wise Analysis")

    sales_cat = df.groupby("Category")

    st.text("Total Sales acc to category :")
    vz_tot_sales = sales_cat["Sales"].sum()
    st.write(vz_tot_sales)

    fig1, ax1 = plt.subplots()
    ax1.bar(vz_tot_sales.index, vz_tot_sales.values)
    ax1.set_title("Total Sales acc to Category")
    st.pyplot(fig1)

    st.text("Total Profit acc to category :")
    vz_tot_profit = sales_cat["Profit"].sum()
    st.write(vz_tot_profit)

    fig2, ax2 = plt.subplots()
    ax2.bar(vz_tot_profit.index, vz_tot_profit.values)
    ax2.set_title("Total Profit acc to Category")
    st.pyplot(fig2)

    # ---------------------------
    # Group by Region
    # ---------------------------
    st.subheader("🌍 Region-wise Analysis")

    region_details = df.groupby("Region")

    reg_sales = region_details["Sales"].sum()
    st.text("Total Sales acc to Region :")
    st.write(reg_sales)

    fig3, ax3 = plt.subplots()
    ax3.barh(reg_sales.index, reg_sales.values)
    ax3.set_title("Total Sales by Region")
    st.pyplot(fig3)

    reg_profit = region_details["Profit"].sum()
    st.text("Total Profit acc to Region :")
    st.write(reg_profit)

    fig4, ax4 = plt.subplots()
    ax4.barh(reg_profit.index, reg_profit.values)
    ax4.set_title("Total Profit acc to Region")
    st.pyplot(fig4)

    # ---------------------------
    # Group by Year
    # ---------------------------
    st.subheader("📅 Yearly Sales")

    grp_year = df.groupby("Order_Year")
    year_sal = grp_year["Sales"].sum()
    year_sal = year_sal.sort_index()

    st.write(year_sal)

    fig5, ax5 = plt.subplots()
    ax5.plot(year_sal.index, year_sal.values, marker="o")
    ax5.set_title("Yearly Sales")
    ax5.set_xlabel("Year")
    ax5.set_ylabel("Total Sales")
    ax5.set_xticks(year_sal.index)
    ax5.grid(True)
    st.pyplot(fig5)

    # ---------------------------
    # Monthly Sales
    # ---------------------------
    st.subheader("📆 Monthly Sales")

    grp_monthly = df.groupby("Order_Month")
    monthly_sale = grp_monthly["Sales"].sum()
    monthly_sale = monthly_sale.sort_index()

    st.write(monthly_sale)

    fig6, ax6 = plt.subplots()
    ax6.plot(monthly_sale.index, monthly_sale.values, marker="o")
    ax6.set_title("Monthly Sales")
    ax6.set_xlabel("Month")
    ax6.set_ylabel("Total Sale")
    ax6.set_xticks(monthly_sale.index)
    ax6.grid(True)
    st.pyplot(fig6)

else:
    st.info("👆 Upload a CSV file to start the analysis")
