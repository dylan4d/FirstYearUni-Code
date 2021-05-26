from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

Census_Data = pd.read_csv('income.csv')

#Is a higher level of education worth it?

for educate in Census_Data.education.unique():
    income_education = Census_Data['income >50K'][Census_Data.education==educate]

lst_education = [education for education in Census_Data.education.unique()]
lst_means = [np.mean(Census_Data['income >50K'][Census_Data.education==educate]) for educate in lst_education]

sorted_means = sorted(zip(lst_means, lst_education), reverse=True)
lst_education = [x[1] for x in sorted_means]
lst_means = [x[0] for x in sorted_means]

education_counts = Census_Data.education.value_counts()
education_counts = education_counts[lst_education]/len(Census_Data)



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
plt.clf()


'''Shows that the higher the education level the more likely you are to earn over 50K yearly. It also shows the proportion of people getting each level of education so you are able to visualise the numbers stopping at each education level. It shows interestingly that
some education like vocational school can have a marginal difference on earning over 50K yearly. However, the data does not show the average or median salary, just binary for over 50K.'''

#Do Immigrants work more?


Census_Data_Immigrants = Census_Data[Census_Data['native-country'] != 'United-States']
Census_Data_Americans = Census_Data[Census_Data['native-country'] == 'United-States']
#print(Census_Data_Immigrants)
#print(Census_Data_Americans)
Census_Data_Immigrants = Census_Data_Immigrants.dropna(subset = ['native-country'])


print(Census_Data_Immigrants['hours-per-week'].describe())
print(Census_Data_Americans['hours-per-week'].describe())


'''Immigrants working less according to the data? The mean for immigrants was lower, however only marginally. The interquartile range was quite similar although the 75th percentile of Americans worked 45hrs weekly, while the 75th
percentile of immigrants worked 40 hours. This could be due to inaccurate data, smaller sample size (although immigrants by definition will be smaller in population), or an under reporting of hours worked by immigrants. This would
be worrying as it shows something more sinister, such as reporting less in order to keep their jobs. Ideally, this should not be happening. Im unsure if this would apply to census data. There would be no need to underreport, for
what I know.'''

Census_Data_Americans_workweek = Census_Data_Americans['hours-per-week'].mean()
Census_Data_Immigrants_workweek = Census_Data_Immigrants['hours-per-week'].mean()
plt.style.use('seaborn-darkgrid')
plt.bar(['American', 'Immigrant'], [Census_Data_Americans_workweek, Census_Data_Immigrants_workweek], color=['#7400B8', '#64DFDF'], width=0.95)
plt.title('American And Immigrant Working Hours')
plt.ylabel('Mean Weekly Hours')
plt.xlabel(f' {round(Census_Data_Americans_workweek, 2)} VS {round(Census_Data_Immigrants_workweek, 2)}')
plt.show()

'''A graphical demonstration between the means of the two groups. Although the difference between the means of the group is marginal as fuck. Not even a fair comparison to make when they are this close. Its literally only a few
minutes. This is also due to the fact that immigrants would be more likely to underreport hours than Americans, however it is also possible that Americans underreport for the same reasons.'''

