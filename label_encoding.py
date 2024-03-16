from sklearn.preprocessing import LabelEncoder

# Create a label encoder object
le = LabelEncoder()

## Assign numerical values and sorting in another column 

data['Urban_Code_mode_encoded'] = le.fit_transform(data['Urban_Code_mode'])

# First, let's list all current columns to understand their order
current_columns = data.columns.tolist()

# Define the desired position for 'Urban_Code_mode_encoded' - right after 'Urban_Code_mode'
# Find the index of 'Urban_Code_mode' and add 1 to get the desired position for 'Urban_Code_mode_encoded'
urban_code_mode_index = current_columns.index('Urban_Code_mode') + 1

# Now, let's remove 'Urban_Code_mode_encoded' from its current position and insert it at the desired position
current_columns.remove('Urban_Code_mode_encoded')  # Remove the encoded column from its current position
current_columns.insert(urban_code_mode_index, 'Urban_Code_mode_encoded')  # Insert it right after 'Urban_Code_mode'

# Reorder the DataFrame columns based on the updated list
data = data[current_columns]

# Display the DataFrame to verify the new column order
data.head(10)


# Display the updated DataFrame to check if the transformation is applied as expected
data.head(10)
