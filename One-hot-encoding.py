import pandas as pd

# Assuming 'data' is your DataFrame

# Create dummy variables for 'Urban_Code_mode'. No 'dtypes' argument is available, so we'll convert dtypes afterwards
urban_code_dummies = pd.get_dummies(data['Urban_Code_mode'], prefix='Urban_Code_mode')

# Convert dummy variables to int
urban_code_dummies = urban_code_dummies.astype(int)

# Concatenate the dummy variables with the original DataFrame
data_with_dummies = pd.concat([data, urban_code_dummies], axis=1)

# Optionally, drop the original 'Urban_Code_mode' column if it's no longer needed
data_with_dummies.drop('Urban_Code_mode', axis=1, inplace=True)

# No direct method to reorder columns alongside the original automatically if it's removed. 
# You would manually specify the order if needed, or keep the transformation logic simple as shown.

# Display the DataFrame to verify the new column order and the dummy variables
data_with_dummies.head(10)
