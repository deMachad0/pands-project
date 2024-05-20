# Analysing iris.data file project
# Author : Andre Machado

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Indicating the directory where the file is 
path = '../pands-project/'
file_name_iris = path + 'iris.data'

# Reading the file 
df = pd.read_csv(file_name_iris)
# removing from the file(iris.data) values that are missing
df.dropna(inplace=True)
# printing the DataFrame and descriptive statistics 'describe()'
print(df)
print(df.describe())

# getting the iris plant sample quantity
sample_quantity = df.shape[0]
print("\nNumber of Iris plant data sample: ")
print(sample_quantity)

# getting the number of plant classes 
class_quantity = df.groupby('class')
print("\nNumber of Iris plant classes: ")
print(len(class_quantity))


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
# importing seaborn using 'height=' to output and fit in 
# one windown
sns.pairplot(df, hue='class', height=1)
plt.savefig('pair_plot.png')
plt.show()