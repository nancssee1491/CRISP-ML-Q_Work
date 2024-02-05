# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:08:09 2023

@author: Nancssee
"""


'''Q1)a. Skewness and Kurtosis: Cars speed and distance'''
# Import Pandas for file reading Statistics calculations:
import pandas as pd

# Importing & reading of dataset Q1_a:
Q1_a= pd.read_csv("C:/Users/hanna/OneDrive/Desktop/Nancssee/Courses/Diploma In Practical Data Analytics/CRISP-ML(Q)/Assignments-CRISP-ML(Q)/Data sets/Data Sets/Q1_a/Q1_a.csv")

# Skewness and Kurtosis of cars speed:
Q1_a.speed.skew()
Q1_a.speed.kurt()

# Skewness and Kurtosis of cars distance:
Q1_a.dist.skew()
Q1_a.dist.kurt()


'''Q1)b. Skewness and Kurtosis: Top Speed (SP) and Weight (WT)'''
# Importing & reading of dataset Q2_b:
Q2_b= pd.read_csv("C:/Users/hanna/OneDrive/Desktop/Nancssee/Courses/Diploma In Practical Data Analytics/CRISP-ML(Q)/Assignments-CRISP-ML(Q)/Data sets/Data Sets/Q2_b/Q2_b.csv")

# Skewness and Kurtosis of Top Speed (SP):
Q2_b.SP.skew()
Q2_b.SP.kurt()

# Skewness and Kurtosis of Weight (WT):
Q2_b.WT.skew()
Q2_b.WT.kurt()


'''Q3) Below are the scores obtained by a student on tests 
34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56

1)	Find the mean, median, variance, and standard deviation.'''
# List down all scores:
scores= [34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56] 

# Convert list into Pandas series:
import pandas as pd
scoresPD= pd.Series(scores)

# Calculate mean, median, variance and standard deviation, and print the outputs:
mean= scoresPD.mean()
print(mean)

median= scoresPD.median()
print(median)

variance= scoresPD.var()
print(variance)

standard_deviation= scoresPD.std() 
print(standard_deviation)      


'''Q10) What will be the IQR of the data (approximately)?'''
# Find Q1 & Q3 by boxplot visualization:
Q1= 10  
Q3= 18

# IQR = Interquartile Rage = Q3-Q1:
IQR= Q3-Q1
print('IQR of the data (approximately) is', IQR) 

'''
Q12) 
(i) What is inter-quartile range of this dataset? [Hint: IQR = Q3 – Q1]'''
# Find Q1 & Q3 by from the boxplot:
Q1= 5
Q3= 12.5

# IQR = inter-quartile range = Q3-Q1:
IQR= Q3-Q1
print('Inter-quartile range of this dataset is', IQR) 

