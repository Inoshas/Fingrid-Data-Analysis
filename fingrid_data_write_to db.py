import pandas as pd
import os
import sqlite3
import json


# Replace 'file.xlsx' with the path to your Excel file
file_path = 'C:/Users/Inosha/Fingrid_data/Small-scale electricity surplus production by production type at accounting points in Finnish distribution networks.xlsx'


# Check if the file exists
if os.path.exists(file_path):
    print(f"File found at: {os.path.abspath(file_path)}")
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        print(df.head())
    except Exception as e:
        print(f"Error reading the file: {e}")
else:
    print(f"File not found: {os.path.abspath(file_path)}")
df['date'] = pd.to_datetime(df['endTime']).dt.date  # Extract the date part
df['time'] = pd.to_datetime(df['endTime']).dt.time  # Extract the time part
df['ProductionType'] = df['additionalJson'].apply(lambda x: json.loads(x).get('ProductionType'))


# Rearrange columns to create the desired table
new_df = df[['date', 'time', 'production','ProductionType' ]]

# Rename columns for better clarity (optional)
new_df.columns = ['Date', 'Time', 'Amount(KWH)', 'ProductionType']

# Display the transformed DataFrame
print(new_df.head())

# Extract special details in additional infor column

# Specify the database name
db_name = 'C:/Users/Inosha/Fingrid_data/electricity_data.db'

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect(db_name)

# Specify the table name where you want to save the data
table_name = "small_scale_production_KWH"

# Save the DataFrame to the database
new_df.to_sql(table_name, conn, if_exists='replace', index=False)

print(f"Data successfully saved to table '{table_name}' in database '{db_name}'.")

# Close the database connection
conn.close()

conn = sqlite3.connect('C:/Users/Inosha/Fingrid_data/electricity_data.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)
conn.close()



