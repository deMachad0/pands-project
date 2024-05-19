# Analysing iris.data file project
# Author : Andre Machado

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Indicating the directory where the file is 
path = '../pands-project/'
file_name_iris = path + 'iris.data'

df = pd.read_csv(file_name_iris)
# removing from the file(iris.data) values that are missing
df.dropna(inplace=True)
# removing the duplicate values from the list
df.drop_duplicates(inplace=True)
# printing the DataFrame and descriptive statistics 'describe()'
print(df)
print(df.describe())

# getting the average using mean()
mean_values = df.groupby('class').mean()
print("\n Average of each class of iris plant: ")
print(mean_values)

# Saving a histogram of each variable to png files
plt.hist(df['sepal length'])
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.savefig('hist_sepal_length.png')
plt.show()

plt.hist(df['sepal width'])
plt.title("Sepal Width Distribution")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.savefig('hist_sepal_width.png')
plt.show()

plt.hist(df['petal length'])
plt.title("Petal Length Distribution")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.savefig('hist_petal_length.png')
plt.show()

plt.hist(df['petal width'])
plt.title("Petal Width Distribution")
plt.xlabel("Petal Width")
plt.ylabel('Frequency')
plt.savefig('hist_petal_width.png')
plt.show()

# Outputing a scatter plot of each pair of variables
# importing seaborn using 'size=' to output and fit in 
# one windown
sb.pairplot(df, hue='class', size=1.7)
plt.show()
plt.savefig('scatter_plot.png')
