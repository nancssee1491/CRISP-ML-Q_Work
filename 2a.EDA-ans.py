# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:07:13 2023

@author: Nancssee
"""


'''Q1)a. Mean and Standard Deviation: Cars speed and distance'''
# Import Pandas for file reading and Statistics calculation:
import pandas as pd

# Importing & reading of dataset Q1_a:
Q1_a= pd.read_csv("C:/Users/hanna/OneDrive/Desktop/Nancssee/Courses/Diploma In Practical Data Analytics/CRISP-ML(Q)/Assignments-CRISP-ML(Q)/Data sets/Data Sets/Q1_a/Q1_a.csv")

# Mean & standard deviation of cars speed:
Q1_a.speed.mean()
Q1_a.speed.std()

# Mean & standard deviation of cars distance:
Q1_a.dist.mean()
Q1_a.dist.std()


'''Q1)b. Mean and Standard Deviation: Top Speed (SP) and Weight (WT)'''
# Importing & reading of dataset Q2_b:
Q2_b= pd.read_csv("C:/Users/hanna/OneDrive/Desktop/Nancssee/Courses/Diploma In Practical Data Analytics/CRISP-ML(Q)/Assignments-CRISP-ML(Q)/Data sets/Data Sets/Q2_b/Q2_b.csv")

# Mean & standard deviation of Top Speed (SP):
Q2_b.SP.mean()
Q2_b.SP.std()

# Mean & standard deviation of Weight (WT):
Q2_b.WT.mean()
Q2_b.WT.std()


'''Q2) Below are the scores obtained by a student on tests. 
34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56

1) Find the mean, median and mode, variance, and standard deviation.'''
# List down all scores:
scores= [34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56] 

# Convert list into Pandas series:
import pandas as pd
scoresPD= pd.Series(scores)

# Calculate mean, median and mode, variance, standard deviation and print the outputs:
mean= scoresPD.mean()
print(mean)

median= scoresPD.median()
print(median)

mode= scoresPD.mode()
print(mode)

variance= scoresPD.var()
print(variance)

standard_deviation= scoresPD.std() 
print(standard_deviation)  
    
    
'''Q3) Three Coins are tossed, find the probability that two heads and one tail are obtained.'''
# Total possible outcomes when 1 coin is tossed:
total1= 2   # Head(H) or Tail(T)

# Total possible outcomes when 3 coins are tossed:
total3= 2**3

# Possible outcomes when 3 coins are tossed, with 2 heads and 1 tail:
total_2H1T= ['HHT', 'HTH', 'THH']

# Probability when 3 coins are tossed, with 2 heads and 1 tail:
probability_2H1T= len(total_2H1T)/total3
print(probability_2H1T)


'''Q4) Two Dice are rolled, find the probability that the sum is

a) Equal to 1'''
# Total possible outcomes for rolling 1 dice:
total1= 6   # Number 1 to 6

# Total possible outcomes for rolling 2 dices:
total2= 6**2

# Total possible outcomes for rolling 2 dices with sum equal to 1:
sum1= 0     # minimum sum is 2

# Probability for rolling 2 dices with sum equal to 1:
probability_sum1= sum1/total2
print(probability_sum1)


'''b) Less than or equal to 4'''
# Possible outcomes for rolling 2 dices with sum less than or euqal to 4:
sum4= [(1,1), (1,2), (1,3), (2,1), (2,2), (3,1)]

# Probability for rolling 2 dices with sum less than or euqal to 4:
probability_sum4= len(sum4)/total2
print(probability_sum4)


'''c) Sum is divisible by 2 and 3'''
# Possible outcomes for rolling 2 dices with sum divisible by 2 and 3:
sum2_3= [(1,5), (2,4), (3,3), (4,2), (5,1), (6,6)]

# Probability for rolling 2 dices with sum divisible by 2 and 3:
probability_sum2_3= len(sum2_3)/total2
print(probability_sum2_3)


'''Q5) A bag contains 2 red, 3 green, and 2 blue balls. Two balls are drawn at random. 
       What is the probability that none of the balls drawn is blue?'''
# import 'math' for combinations(binomial coefficient) calculation:
import math
    
# Total of balls:
red= 2    
green= 3
blue= 2
total_red_green= red+green      
total_all= red+green+blue

# Total ways to draw 2 balls:
total_2= math.comb(total_all, 2)
 
# Total ways to draw 2 balls without blue:     
total_2_non_blue= math.comb(total_red_green, 2)       

# Probability which none of the balls drawn is blue:
Probability_2_non_blue= total_2_non_blue/total_2   
print(Probability_2_non_blue)       


'''Q6) Calculate the Expected number of candies for a randomly selected child:'''       
# Define probabilities of having X number of candies into a dictionary, PX. 
# (Probability of having 1 candy is 0.015, etc.):
PX= {1:0.015, 4:0.20, 3:0.65, 5:0.005, 6:0.01, 2:0.12}  
                                                             
# Calculate expected value with sum(X*P(X)), with X=keys, P(X)=values:
expected_value= sum(keys*values for keys, values in PX.items())
print("Expected number of candies for a randomly selected child is", expected_value)      


'''Q7) Calculate the Expected Value for the problem below.
a) The weights (X) of patients at a clinic (in pounds), are:
108, 110, 123, 134, 135, 145, 167, 187, 199
Assume one of the patients is chosen at random. What is the Expected Value 
of the Weight of that patient?'''
# Define Weights into a list, X:
X= [108, 110, 123, 134, 135, 145, 167, 187, 199]

# Import Pandas to convert list into series:
import pandas as pd
X_pd= pd.Series(X)

# Since expected value = mean:
expected_value= X_pd.mean()
print(f'Expected Value of the Weight of that patient is {expected_value} pounds.')


'''Q8) Look at the data given below. Plot the data, find the outliers, and find out: μ,σ,σ^2
Hint: [Use a plot that shows the data distribution, and skewness along with the 
      outliers; also use Python code to evaluate measures of centrality and spread]'''

# Define data into dictionary X:
X= {'Name of company':['Allied Signal','Bankers Trust','General Mills','ITT Industries',
                       'J.P.Morgan & Co.','Lehman Brothers','Marriott','MCI','Merrill Lynch',
                       'Microsoft','Morgan Stanley','Sun Microsystems','Travelers',
                       'US Airways','Warner-Lambert'],
    'Measure X':[24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,
                 25.99,39.42,26.71,35.00]}     
 
# Import Pandas to convert X into dataframe:
import pandas as pd
X_df= pd.DataFrame(X)
print(X_df)
      
# Import Matplotlib to plot boxplot:       
import matplotlib.pyplot as plt      

plt.boxplot(X_df['Measure X'])
plt.xlabel('Dataset No.')
plt.ylabel('Percentage(%)')      
plt.title('Boxplot of Measure X')       
plt.show()   

# Observe outlier from boxplot, and identify it by matching it with data:
'''Yes, there is 1 outlier, which is:''' 
outlier_X_df= {'Morgan Stanley': 91.36}

# Find μ,σ,σ^2:
mean_X_df= X_df['Measure X'].mean()    
print(mean_X_df)

standard_deviation_X_df= X_df['Measure X'].std()    
print(standard_deviation_X_df)

variance_X_df= X_df['Measure X'].var()    
print(variance_X_df)


'''Q9) Suppose that one in 200 long-distance telephone calls is misdirected. 
What is the probability that at least one in five attempted telephone calls 
reaches the wrong number? (Assume independence of attempts.)
Hint: [Using the Probability formula evaluate the probability of one call being 
       wrong out of five attempted calls]'''

'''Solution 1: using binomial probability'''
# Import 'math' to count combinations:
import math

# Probability where 1 call is wrong:
p= 1/200

# Total attempted calls:
n= 5

# Probability where at least 1 in 5 calls is wrong:
wrong_at_least_1= sum(math.comb(n,k) * (p**k) * ((1-p)**(n-k)) for k in range(1, n+1))
print(wrong_at_least_1)


'''Solution 2: using probability complementary concept'''
# Probability where 1 call is wrong:
wrong1= 1/200

# Probability where 1 call is right:
right1= 1-wrong1

# Probability where 5 calls are right (when all 5 calls are right, with 0 wrong):
right5= right1**5      
    
# Probability where at least 1 in 5 calls is wrong:
wrong1_at_least= 1-right1**5
print(wrong1_at_least)


'''Q10) Returns on a certain business venture, to the nearest $1,000, are known 
to follow the following probability distribution.

(i) What is the most likely monetary outcome of the business venture?
Hint: [The outcome is most likely the expected returns of the venture]'''

# Define the probability distribution into a dictionary:
PX= {-2000:0.1, -1000:0.1, 0:0.2, 1000:0.2, 2000:0.3, 3000:0.1} 

# Calculate expected returns (the most likely business venture monetary outcome):
expected_returns= sum(keys*values for keys, values in PX.items())
print(f"The most likely monetary outcome of the business venture is ${expected_returns}."
    ,"When rounded to the nearest $1,000, it is $1,000.")


'''(ii)	Is the venture likely to be successful?
Hint: [Probability of % of the venture being a successful one]'''

# Refer to PX from (i), only for values with keys > 0, sum up those values: 
PX= {-2000:0.1, -1000:0.1, 0:0.2, 1000:0.2, 2000:0.3, 3000:0.1}
PX_positive = sum(values for keys, values in PX.items() if keys > 0)
print(PX_positive)


'''(iv) Compute this measure. 
Hint: [Risk here stems from the possible variability in the expected returns, 
       therefore, name the risk measure for this venture]'''

'''Answer: Good measure of the risk is standard deviation, σ.'''

# Refer to PX and expected_returns from (i), calculate the variance:
PX= {-2000:0.1, -1000:0.1, 0:0.2, 1000:0.2, 2000:0.3, 3000:0.1} 
expected_returns= sum(keys*values for keys, values in PX.items())
variance= sum(values * (keys-expected_returns)**2 for keys, values in PX.items())    

# Calculate standard deviation by square root the variance:
standard_deviation= variance**(1/2)   
print('The standard deviation (the measure of risk) is',standard_deviation)

