## Visualization 

### Choosing the Right Plot Type: Select a plot type that best represents your data. Common types include:

### Line Plot: For continuous data, showing trends over time.
### Bar Plot: For categorical data, showing comparisons.
### Histogram: For distribution of a single variable.
### Scatter Plot: For relationships between two variables.
### Labeling: Ensure your plot is well-labeled:

### Title: Describes what the plot represents.
### Axis Labels: Describes the data on each axis.
### Legend: Identifies different data series or categories if there are multiple.
### Scaling: Make sure the scales on your axes are appropriate for the data being presented. Use logarithmic scales if needed.

### Colors and Styles: Use colors and line styles to differentiate between different data series. Ensure the colors are distinguishable and accessible.

### Grid and Layout: Adding grid lines can help with readability. Ensure the layout is clean and uncluttered.

#### Here's a step-by-step guide to creating a basic plot using Matplotlib:

## Import Matplotlib: 
import matplotlib.pyplot as plt

## Prepare Data: Ensure your data is in the correct format (e.g., lists, arrays, or pandas DataFrames)

## Create a Figure and Axes: 
fig, ax = plt.subplots()  # Create a figure and an axes.

## Plot Data: 
ax.plot(x, y, label='Label for data')  # For line plot
ax.bar(categories, values)  # For bar plot
ax.scatter(x, y)  # For scatter plot

## Labeling: 
ax.set_title('Title of the Plot')
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.legend(loc='best')  # Add legend.

## Grid and Layout: 
ax.grid(True)  # Add grid lines.
fig.tight_layout()  # Adjust layout to prevent clipping.

## Show the Plot: 
plt.show()  # Display the plot.


### Problem -2: 
import matplotlib.pyplot as plt

# Step 1: Count the unique elements and their frequencies
source_title_counts = yes_dataset['Source title'].value_counts()

# Step 2: Limit the number of source titles shown (e.g., top 20)
top_source_title_counts = source_title_counts.head(20)

# Step 3: Create a horizontal bar plot with the top source titles
fig, ax = plt.subplots(figsize=(10, 8))
top_source_title_counts.plot(kind='barh', ax=ax)

# Step 4: Add labels and title
ax.set_xlabel('Count', fontsize=12, fontname='Times New Roman')
ax.set_ylabel('Source title', fontsize=12, fontname='Times New Roman')
ax.set_title('Top 20 Source Titles in yes_dataset', fontsize=14, fontname='Times New Roman')

# Step 5: Add values on top of each bar
for i in ax.patches:
    ax.text(i.get_width() + 0.3,  # Adjust the position of the text
             i.get_y() + i.get_height() / 2,
             str(int(i.get_width())),
             fontsize=10,
             color='black',
             va='center',
             fontname='Times New Roman')

# Step 6: Adjust layout for better fit and display the plot
plt.tight_layout()
plt.show()

