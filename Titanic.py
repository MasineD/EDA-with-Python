'''
    PURPOSE:
        1.This contains the python cold code used to answer the stakeholder questions based on the provided 
          datasets
    
    WARNING:
        1.You must ensure that you have all the python modules used in this script installed on you local machine
          before running the code that follows
'''

import pandas as pd
import matplotlib.pyplot as plt     #used to draw visualizations

# Creating a data frame
df = pd.read_csv(r"C:\Users\Donald\OneDrive\Documents\DataAnalysis\EDAwithPython-Titanic\Titanic.csv")

first10rows = df.head(10)   # Getting the first 10 rows
last10rows = df.tail(10)    # Getting the last 10 rows

shapeOfDate = df.shape  #Getting the shape of the data

columnNames = df.columns    # Getting all the columns names
columnTypes = df.dtypes # Getting the data type of all columns

details = df.describe   #Getting detailed information and summary
summary = df.info()

# Counting the survivors  and presenting the results in a pie chart
survivors = df.Survived.value_counts()
survivorsLabels = 'Not survived', 'Survived'

figure1 = plt.figure(1)     #Use figures to avoid overlapping
plt.pie(survivors, autopct = "%0.2f%%", labels = survivorsLabels, shadow = True)
plt.title('Survivors-vs-Non survivors')
print(plt.show())

# Finding female passengers across different classes and presenting results in a pie chart
females = df[df.Sex == 'female']
femalesClass = females.Pclass.value_counts()
femaleClassLabels = '3rd class','1st class','2nd class'

figure2 = plt.figure(2)     
plt.pie(femalesClass, autopct = '%0.1f%%', labels = femaleClassLabels, explode = (0,0.05,0))
plt.title('Female passenger classes')
print(plt.show())

# Finding female survivors younger than 30 and presenting results on pie and bar chart
youngFemales_30 = females[females.Age < 30]
youngFemaleSurvivors = youngFemales_30.Survived.value_counts()

figure3 = plt.figure(3)  
youngFemalesLabels = 'Survived','Not survived'
plt.pie(youngFemaleSurvivors, autopct = '%0.1f%%', labels = youngFemalesLabels, colors = ['#00C0A3','#FF4500'])
plt.title('Female survivors younger than 30')
print(plt.show())

# Finding male survivors younger than 40 and presenting results on pie chart
youngMalesSurvivors_40 = df[(df.Sex == 'Male') & (df.Age < 40)]
youngMalesSurvivors = youngMalesSurvivors_40.Survived.value_counts()

figure4 = plt.figure(4)
youngMalesLabels = 'Survived', 'Not survived'
plt.pie(youngMalesSurvivors, autopct='%0.1f%%', colors=['#00C0A3', '#FF4500'])
plt.title('Male survivors younger than 40')
print(plt.show())
