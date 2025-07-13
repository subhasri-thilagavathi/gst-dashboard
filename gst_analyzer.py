import pandas as pd

# Load Excel file (update path if needed)
file_path = "gst_invoices.xlsx"
df = pd.read_excel(file_path)

# Show first 5 rows
print("🔹 First few rows:")
print(df.head())

# Total Taxable Value
total_taxable = df["Taxable Value"].sum()
print(f"\n✅ Total Taxable Value: ₹{total_taxable}")

# Total GST breakdown
total_cgst = df["CGST"].sum()
total_sgst = df["SGST"].sum()
total_igst = df["IGST"].sum()

print(f"✅ Total CGST: ₹{total_cgst}")
print(f"✅ Total SGST: ₹{total_sgst}")
print(f"✅ Total IGST: ₹{total_igst}")
print(f"✅ Total GST Collected: ₹{total_cgst + total_sgst + total_igst}")

# Flag missing GSTINs
missing_gstin = df[df["GSTIN"].isnull()]
print(f"\n⚠️ Invoices with missing GSTINs:\n{missing_gstin[['Invoice No', 'Party Name']]}")
