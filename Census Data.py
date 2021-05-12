from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

income = pd.read_csv('income.csv')

#print(np.mean(income.age)) mean AGE is 38.6


for educate in income.education.unique():
    income_education = income['income >50K'][income.education==educate]

lst_education = [education for education in income.education.unique()]
lst_means = [np.mean(income['income >50K'][income.education==educate]) for educate in lst_education]

sorted_means = sorted(zip(lst_means, lst_education), reverse=True)
lst_education = [x[1] for x in sorted_means]
lst_means = [x[0] for x in sorted_means]

education_counts = income.education.value_counts()
education_counts = education_counts[lst_education]/len(income)



plt.style.use('seaborn-darkgrid')

plt.subplot(2,1,1)
plt.bar(lst_education, lst_means, color = ['#7400B8', '#6930C3', '#5E60CE', '#5390D9', '#4EA8DE', '#48BFE3', '#56CFE1', '#64DFDF', '#72EFDD', '#80FFDB'])
plt.ylabel('Percentage Earning Over 50K')
plt.title('How Education Levels Impact The Proportion Earning Over 50K')

plt.subplot(2,1,2)
education_counts.plot.bar(color = ['#7400B8', '#6930C3', '#5E60CE', '#5390D9', '#4EA8DE', '#48BFE3', '#56CFE1', '#64DFDF', '#72EFDD', '#80FFDB'])
plt.title('Comparison of The Popularity of Education Levels')
plt.xlabel('Maximum Education Earned')
plt.ylabel('Percentage Obtaining Education Level')

plt.show()

