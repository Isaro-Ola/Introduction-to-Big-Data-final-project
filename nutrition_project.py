import pandas as pd
import re
import numpy as np

# ✅ 1. Load the CSV file
df = pd.read_csv("nutrition_indicators_rwa.csv")

# ✅ 2. Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.rename(columns={'gho_(display)': 'indicator'}, inplace=True)

# ✅ 3. Clean value column
df['value'] = df['value'].astype(str).str.extract(r'(\d+\.?\d*)')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# ✅ 4. Remove metadata and fix year column
df = df[df['indicator'] != '#indicator+name']
df = df[df['year_(display)'] != '#date+year']
df['year_(display)'] = pd.to_numeric(df['year_(display)'], errors='coerce')

# ✅ 5. Filter anaemia records
anaemia_df = df[df['indicator'].str.contains('anaemia in children', case=False)]
anaemia_df = anaemia_df.dropna(subset=['value'])

# ✅ 6. Filter stunting
stunting_df = df[df['indicator'].str.contains('stunting', case=False)]
stunting_df = stunting_df.dropna(subset=['value'])
stunting_df.to_csv("cleaned_stunting_data.csv", index=False)
print("✅ Exported cleaned_stunting_data.csv")

# ✅ 7. Filter underweight
underweight_df = df[df['indicator'].str.contains('underweight', case=False)]
underweight_df = underweight_df.dropna(subset=['value'])
underweight_df.to_csv("cleaned_underweight_data.csv", index=False)
print("✅ Exported cleaned_underweight_data.csv")

# ✅ 8. Save cleaned anaemia data to CSV for Power BI
anaemia_df.to_csv("cleaned_anaemia_data.csv", index=False)

print("✅ Clean anaemia data exported to 'cleaned_anaemia_data.csv'")

