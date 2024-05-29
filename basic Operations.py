## How to insert 

df.columns.get_loc('Abstract') 

# Apply the preprocessing function to the 'Abstract' column
df['clean_text'] = df['Abstract'].apply(lambda x: apply_preprocessing(x))

# Move the 'clean_text' column to the second position
df.insert(1, 'clean_text', df.pop('clean_text'))
