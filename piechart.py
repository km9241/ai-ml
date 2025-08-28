import matplotlib.pyplot as plt

plt.rcdefaults()  # Resets matplotlib to default style

# Data
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']  # red, green, blue, cyan, magenta
explode = [0, 0, 0.2, 0, 0]  # 'Russia' slice is slightly separated by 20percent
labels = ['India', 'United States', 'Russia', 'China', 'Europe']
# Plotting the pie chart
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title('Student Locations')
plt.show()