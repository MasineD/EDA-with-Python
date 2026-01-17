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
import numpy as np

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

figure15 = plt.figure(15)     #Use figures to avoid overlapping
plt.pie(survivors, autopct = "%0.2f%%", labels = survivorsLabels, shadow = True)
plt.title('Survivors-vs-Non survivors')
print(plt.show())

# Finding female passengers across different classes and presenting results in a pie chart
females = df[df.Sex == 'female']
femalesClass = females.Pclass.value_counts()
femaleClassLabels = '3rd class','1st class','2nd class'

figure14 = plt.figure(14)     
plt.pie(femalesClass, autopct = '%0.1f%%', labels = femaleClassLabels, explode = (0,0.05,0))
plt.title('Female passenger classes')
print(plt.show())

# Finding female survivors younger than 30 and presenting results on pie and bar chart
youngFemales_30 = females[females.Age < 30]
youngFemaleSurvivors = youngFemales_30.Survived.value_counts()

figure13 = plt.figure(13)  
youngFemalesLabels = 'Survived','Not survived'
plt.pie(youngFemaleSurvivors, autopct = '%0.1f%%', labels = youngFemalesLabels, colors = ['#00C0A3','#FF4500'])
plt.title('Female survivors younger than 30')
print(plt.show())

# Finding male survivors younger than 40 and presenting results on pie chart
youngMalesSurvivors_40 = df[(df.Sex == 'Male') & (df.Age < 40)]
youngMalesSurvivors = youngMalesSurvivors_40.Survived.value_counts()

figure12 = plt.figure(12)
youngMalesLabels = 'Survived', 'Not survived'
plt.pie(youngMalesSurvivors, autopct='%0.1f%%', colors=['#00C0A3', '#FF4500'])
plt.title('Male survivors younger than 40')
print(plt.show())

# Showing the age with  bins
figure11 = plt.figure(11)
plt.hist(df.Age, bins = 20, color = 'aqua', edgecolor = 'orangered')
plt.xticks(np.arange(0,85,5))
print(plt.show())

# Showing the age frequency of survived passengers
figure10 = plt.figure(10)
ageWithSurvived = df[df.Survived == 1].Age
plt.hist(ageWithSurvived)
print(plt.show())

# Showing a survived males and females on a bar chart
figure9 = plt.figure(9)
survivedMales_Females = dict(df[df.Survived == 1].Sex.value_counts())
xValues = survivedMales_Females.keys()
yValues = survivedMales_Females.values()
plt.bar(xValues, yValues)
# print(survivedMales_Females)
print(plt.show())
# ============ Practise how to create bar chart with Matplotlib=============

# Showing, in a bar chart, how many passengers travelled in each class
figure8 = plt.figure(8)
values = dict(df.Pclass.value_counts())
xValues = values.keys()
yValues = values.values()
plt.bar(xValues, yValues)
print(plt.show())

# Showing how many passengers travelled in different classes
figure7 = plt.figure(7)
passengersAcrossClasses = dict(df.Pclass.value_counts())
xValues = passengersAcrossClasses.keys()
yValues = passengersAcrossClasses.values()
classes = []
for x in xValues:
    if x == 1:
        classes.append('first-class')
    elif x == 2:
        classes.append('second-class')
    elif x == 3:
        classes.append('third-class')
  
plt.bar(classes, yValues)
plt.title('Passengers across different classes')
plt.ylabel('Nr. of passengers')
plt.xlabel('Classes')
print(plt.show())

# Showing, in a bar chart, survivors across different classes
figure6 = plt.figure(6)
survivorsAcrossClasses = dict(df[df.Survived == 1].Pclass.value_counts())
xValues = survivorsAcrossClasses.keys()
yValues = survivorsAcrossClasses.values()

classNames = []
for x in xValues:
    if x == 1:
        classNames.append('first-class')
    elif x == 2:
        classNames.append('second-class')
    elif x == 3:
        classNames.append('third-class')
plt.title('Survivors across different classes')
plt.xlabel('Classes')
plt.ylabel('Nr. of survivors')
plt.bar(classNames, yValues)
print(plt.show())