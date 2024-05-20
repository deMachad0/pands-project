Fisher's Iris dataset

Write a program called analysis.py that:
1. Outputs a summary of each variable to a single text file,
2. Saves a histogram of each variable to png files, and 
3. Outputs a scatter plot of each pair of variables.
4. Performs any other analysis you think is appropriate.

Summary of each variable 
Programming and Scripting Lab Extra 10 - Pandas exercises and classes - it was very useful to help to read the file,
use describe() and get the average values using mean()
https://atu-main-mdl-euwest1.s3.eu-west-1.amazonaws.com/27/02/2702b024905c9ab89836bff8d00e06dcdba0f367?response-content-disposition=inline%3B%20filename%3D%22Lab%2010%20pandas.pdf%22&response-content-type=application%2Fpdf&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWRN6GJFLWCMOG6H7%2F20240519%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240519T142158Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21542&X-Amz-Signature=c3e1060e8a368e213f5a3820cd98f206d2549eb26225bad4f37a9d80224ae5a5
How to use len() and shape[] to be able of counting the sample 
https://stackoverflow.com/questions/17468878/pandas-python-how-to-count-the-number-of-records-or-rows-in-a-dataframe

Histogram 
How to create - https://docs.kanaries.net/topics/Pandas/pandas-plot-histogram 
how to save (png file) - https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python#:~:text=Plot%20the%20histogram%20using%20hist,figure%2C%20use%20show()%20method.
Programming and Scripting Lab Topic 08-plotting exercises and classes
https://atu-main-mdl-euwest1.s3.eu-west-1.amazonaws.com/4a/2f/4a2fd8d23088f9d87b69902e5a31076629cf05cb?response-content-disposition=inline%3B%20filename%3D%22Lab%2008%20matplotlb.pdf%22&response-content-type=application%2Fpdf&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWRN6GJFLWCMOG6H7%2F20240519%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240519T142843Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21557&X-Amz-Signature=4e67b6c15867c68866a4aeae5e5d78f3661d05c7abe18857d529d83ac8074ca8

Scatter plot
how to use pairplot - https://seaborn.pydata.org/generated/seaborn.pairplot.html
https://www.youtube.com/watch?v=uCgvlfIo9fg

Jupyter Notebook
Helpful link to learn how to start with Jupyter Notebook 
https://medium.com/@claudia.nikel/how-to-setup-a-jupyter-notebook-in-vs-code-w-virtual-env-kernels-install-packages-884cf643375e

Conclusion 

   The Iris dataset is very popular and has been used to demonstrate the fundamentals of statistical techniques and machine learning by many developers and Data analysts during the years. 
   In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. According to UCI Machine Learning Repository, the Iris dataset is widely used in pattern recognition learning. 
   Iris dataset has 150 samples in total, 50 samples from each of three species of Iris flowers named Setosa, Versicolor and Virginica, in which they were measured by lengths and the widths of sepals and petals.
   As researched, it can be seen that in the average of iris plant classes, Iris virginica has the highest average sepal length and petal width, followed by Iris versicolor and Iris setosa.
   The pairplot graphic also helps us to see that Iris setosa specie has the smallest petals widths and lengths, and sepal lenght but larger sepal widths if compared to any other species. Where the Iris virginica has the largest petal lengths and widths, while Iris versicolor is in the midle of the three species.
   The tools used in python programming language in this dataset were mean() to find the average of all the species studied, len() to find the quantity of plant species, shape[] to find the exact number of samples and many histograms to help us to indentify each dimension of the species. 

References 

(2023, August 26). Exploring the Iris Dataset: A Journey from Data Loading to Model Building. Medium. Retrieved May 20, 2024, from https://medium.com/@Gayatri2410/exploring-the-iris-dataset-a-journey-from-data-loading-to-model-building-acf099ed4dd7

(2021). About Fisher’s Iris dataset. Angela1c. Retrieved May 20, 2024, from https://www.angela1c.com/projects/iris_project/the-iris-dataset/

(2024, March 20). Exploratory Data Analysis on Iris Dataset. Geeksforgeeks. Retrieved May 20, 2024, from https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

