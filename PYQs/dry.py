import csv
import matplotlib.pyplot as plt
import pandas as pd

# Data as a dictionary
data = {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8419600, 3980400, 2716000],
    'Area': [783.8, 503, 589]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Writing DataFrame to 'cities.csv'
df.to_csv('cities.csv', index=False)

print("Data has been written to cities.csv using pandas")

# Initialize arrays to store the data
city_data = []
last_column_data = []

# Read the CSV file and process data
with open('cities.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row
    header = next(reader)
    
    for row in reader:
        # Check if the row has enough columns to avoid IndexError
        if len(row) < 2:  # Ensure the row has at least two columns
            print(f"Skipping row due to insufficient columns: {row}")
            continue  # Skip this row
        
        # Add all columns except the last one to city_data
        city_data.append(row[:-1])
        
        # Add the last column (Temperature, for example) to last_column_data
        last_column_data.append(row[-1])


# Convert city_data to a numpy array for better handling (optional)
import numpy as np
city_data = np.array(city_data)


# Extract the first two columns for plotting (e.g., City and Population)
first_column = city_data[:, 0]  # First column (City names)
second_column = city_data[:, 1]  # Second column (Population)

# Plot the first two columns
plt.figure(figsize=(10, 6))
plt.scatter(first_column, second_column, color='blue', label='City vs Population')
plt.xlabel('City')
plt.ylabel('Population')
plt.title('City vs Population Plot')
plt.xticks(rotation=90)  # Rotate city names for better readability
plt.tight_layout()
plt.legend()
# plt.show()

# If you want to see the extracted last column data (e.g., Temperature)
print("Last column data (Temperature):", last_column_data)





