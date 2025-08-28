import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
'''Seaborn is a Python data visualization library built on top of matplotlib. 
It makes it easier to create beautiful, informative, and professional-looking plots with less code.'''
sns.set() #We can load up Seaborn, and just call set() on it to change matplotlib's default settings to something more visually pleasing.
#It automatically applies a nice style to your matplotlib plots. Fonts, colors, spacing — all improved.
df = pd.read_csv('C://pythonforml//FuelEfficiency.csv')
gear_counts = df['# Gears'].value_counts() #This line is counting how many times each unique value appears in the # Gears column of your DataFrame.
gear_counts.plot(kind='bar')
plt.show()
sns.distplot(df['CombMPG'])#"distplot" can be used to plot a histogram together with a smooth distribution of that histogram overlaid on it.
plt.show()
df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]#new DataFrame df2 that contains only these four columns:
print(df2.head())#first 5 rows of the new df2 
'''pairplot() creates a grid of scatter plots (and histograms on the diagonal) to visualize pairwise relationships between all columns.'''
sns.pairplot(df2,hue="Cylinders", height=2.5,)
#hue="Cylinders" tells Seaborn to color-code the data points based on the value in the Cylinders column.
#It creates separate colors for each unique value of Cylinders meaning
plt.show()
sns.jointplot(x="Eng Displ", y="CombMPG", data=df)
plt.show()
'''It plots both:
A scatter plot (or other kind of bivariate plot) in the center,
Histograms of each variable on the top (for x) and right (for y).'''
sns.lmplot(x="Eng Displ", y="CombMPG", data=df)
plt.show()#lmplot makes a scatter plot and adds a straight line that shows the trend (a line of best fit).
df2 = df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG', aggfunc='mean')
sns.heatmap(df2)
''' A heat map allows you to plot tabular, 2D data of some sort, with colors representing the individual values in each cell of the 2D table.
In this example, we'll create a pivot table from our original dataframe, to create a 2D table that contains the average MPG ratings for every combination of number of cylinders and engine displacement.
The resulting heatmap shows all of the engine displacement values along the X axis, and all of the cylinder values along the Y axis. For each cell of the table,
 the actual average MPG rating for that combination of cylinders and engine displacement is represented not as a number, but as a color that ranges from dark for small values, and light for larger values.
'''
plt.show()

