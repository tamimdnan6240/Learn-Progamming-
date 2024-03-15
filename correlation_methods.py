import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def calculate_corr(df):
    numeric_data = df.select_dtypes(include='number')
    data_corr_ = numeric_data.corr(method='pearson')
    return data_corr_

def calculate_corr_columns(df, threshold_value):
    # Exclude non-numeric columns before calculating correlations
    numeric_data = df.select_dtypes(include='number')
    data_corr_ = numeric_data.corr(method='pearson')

    find_corr_columns = []

    for index, row in data_corr_.iterrows():
        # Assuming the correlation matrix is square and indexed similarly to columns:
        value = row[row.index != index] > threshold_value
        if value.any():  
            find_corr_columns.append(index)

    # Create a mask to display only the lower triangle
    mask = np.triu(np.ones_like(data_corr_[find_corr_columns], dtype=bool))

    # Plot the heatmap for visualization
    plt.figure(figsize=(30, 18))
    corre_matrix = sns.heatmap(data_corr_[find_corr_columns], annot=True, linewidth=.5,
                               cmap="RdYlGn", center=0, mask=mask)
    plt.title('Correlation Matrix')
    plt.savefig("Correlation Matrix Variables.png")
    plt.show()

    return find_corr_columns, corre_matrix
