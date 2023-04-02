# import pandas as pd

# # Read CSV file into a DataFrame
# df = pd.read_csv('Practise2.csv')

# # Set the model number of interest
# model_no = 'QQP-CHR-7281PM'
# nrp = '100000'
# # Locate the rows corresponding to the model number
# mask = df['PART CODE'] == model_no
# selected_rows = df.loc[mask]

# # Convert the "NRP" column to a numeric data type
# mask = df['NRP'] == nrp
# selected_rows = df.loc[mask]
# selected_rows['NRP'] = pd.to_numeric(selected_rows['NRP'], errors='coerce')
# selected_rows['NRP'] = selected_rows['NRP'].fillna(0)

# # Update the values in the selected rows as needed
# selected_rows['NRP'] += 1

# # Write the updated DataFrame back to the CSV file
# df.to_csv('Practise2.csv', index=False)
import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('Practise2.csv')

# Set the model number of interest
model_no = 'QQP-CHR-7281PM'

# Locate the rows corresponding to the model number
mask = df['PART CODE'] == model_no
selected_rows = df.loc[mask]

# Update the values in the selected rows as needed
df.loc[mask, 'NRP'] = 15000  # set the new MRP value

# Write the updated DataFrame back to the CSV file
df.to_csv('Practise3.csv', index=False)
