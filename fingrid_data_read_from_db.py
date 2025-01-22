import sqlite3

# Connect to the database
conn = sqlite3.connect('C:/Users/Inosha/Fingrid_data/electricity_data.db')

# Query to list tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print all table names
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
