import sqlite3  # Use appropriate library for your database
import pandas as pd

# Connect to the database
connection = sqlite3.connect('C:/Users/Inosha/Fingrid_data/electricity_data.db')
cursor = connection.cursor()

# Query the data
query =  """SELECT 
    Date 
    AVG([Wind Power Generation Forecast]) as Avg_wind_power_per_day
    FROM 
    Wind_power_generation_forecast
    GROUP BY 
    Date
    ORDER BY 
    Date; """
    
cursor.execute(query)



# Fetch all data
data = cursor.fetchall()
columns = [description[0] for description in cursor.description]

# Convert the data into a DataFrame for easier handling

df = pd.DataFrame(data, columns=columns)

# Display the first 10 rows of the DataFrame
#print("First 10 Rows of the Table:\n", df.head(10))  # .head(10) displays the first 10 rows
