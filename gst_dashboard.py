import pandas as pd
import streamlit as st

# Load Excel file
df = pd.read_excel("gst_invoices.xlsx")

st.title("📊 GST Invoice Dashboard")

# Total Stats
st.subheader("✅ GST Collection Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Taxable Value", f"₹{df['Taxable Value'].sum():,.2f}")
col2.metric("Total CGST", f"₹{df['CGST'].sum():,.2f}")
col3.metric("Total SGST", f"₹{df['SGST'].sum():,.2f}")

col4, col5 = st.columns(2)
col4.metric("Total IGST", f"₹{df['IGST'].sum():,.2f}")
col5.metric("Total GST", f"₹{(df['CGST']+df['SGST']+df['IGST']).sum():,.2f}")

# Filter by State
states = df["State"].dropna().unique()
selected = st.selectbox("📍 Filter by State", ["All"] + list(states))

if selected != "All":
    df = df[df["State"] == selected]

# Show filtered data
st.subheader("🧾 Invoices")
st.dataframe(df)

# Missing GSTIN
st.subheader("⚠️ Invoices with Missing GSTIN")
missing = df[df["GSTIN"].isnull()]
st.dataframe(missing[["Invoice No", "Party Name", "State", "Taxable Value"]])
