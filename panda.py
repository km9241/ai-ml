import pandas as pd
import matplotlib.pyplot as plt  # Required for plotting

data = pd.read_csv('C:\\pythonforml\\Name,Age,City.txt')

print(data.head())         # First 5 rows
print(data.head(3))        # First 3 rows
print(data.shape)          # (rows, columns)
print(data.size)           # Total number of cells
print(data.columns)        # Column names

# Sort by Age and display
print(data.sort_values(['Age']))

# Count how many times each Age appears
valueofage = data['Age'].value_counts()

# Plot as bar chart
valueofage.plot(kind='bar')
"""This tells Pandas to draw a bar chart using the valueofage Series.

Each bar represents an age, and its height represents how many people have that age.

kind='bar' specifies it's a vertical bar chart."""

plt.title('Count of Each Age')
plt.xlabel(data.sort_values(['Age']))
plt.ylabel('Frequency')
plt.show()
