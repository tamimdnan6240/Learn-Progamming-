
# Find the index of the column 'Abstract'
index_of_abstract = df.columns.get_loc('Abstract')

# Create the new column order with 'Abstract' moved to the first position
new_order = ['Abstract'] + [col for col in df.columns if col != 'Abstract']

# Reindex the dataframe with the new column order
df = df.reindex(columns=new_order)

print(df)
