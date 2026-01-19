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
import math

# -------------- Question 1 --------------
# Creating a data frame
df = pd.read_csv(r"C:\Users\Donald\OneDrive\Documents\DataAnalysis\EDAwithPython-Titanic\Titanic.csv")

# ------------- Question 2 ---------------
first10rows = df.head(10)   # Getting the first 10 rows
last10rows = df.tail(10)    # Getting the last 10 rows

# ------------- Question 3 ---------------
shapeOfDate = df.shape  #Getting the shape of the data

# ------------- Question 4 ---------------
columnNames = df.columns    # Getting all the columns names

# ------------- Question 5 ---------------
columnTypes = df.dtypes # Getting the data type of all columns

# ------------- Question 6 ---------------
details = df.describe   #Getting detailed information and summary
summary = df.info() 

# ------------- Question 7 ---------------
# Counting the survivors  and presenting the results in a pie chart
survivors = df.Survived.value_counts()
survivorsLabels = 'Not survived', 'Survived'
figure1 = plt.figure(1)     #Use figures to avoid overlapping
plt.pie(survivors, autopct = "%0.2f%%", labels = survivorsLabels, shadow = True)
plt.title('Survivors-vs-Non survivors')
print(plt.show())

# ------------- Question 8 ---------------
# Finding female passengers across different classes and presenting results in a pie chart
females = df[df.Sex == 'female']
femalesClass = females.Pclass.value_counts()
femaleClassLabels = '3rd class','1st class','2nd class'
figure2 = plt.figure(2)     
plt.pie(femalesClass, autopct = '%0.1f%%', labels = femaleClassLabels, explode = (0,0.05,0))
plt.title('Female passenger classes')
print(plt.show())

# ------------- Question 9---------------
# Finding female survivors younger than 30 and presenting results on pie and bar chart
youngFemales_30 = females[females.Age < 30]
youngFemaleSurvivors = youngFemales_30.Survived.value_counts()
figure3 = plt.figure(3)  
youngFemalesLabels = 'Survived','Not survived'
plt.pie(youngFemaleSurvivors, autopct = '%0.1f%%', labels = youngFemalesLabels, colors = ['#00C0A3','#FF4500'])
plt.title('Female survivors younger than 30')
print(plt.show())

# ------------- Question 10 ---------------
# Finding male survivors younger than 40 and presenting results on pie chart
youngerThan40 = df[df.Age < 40]
malesYoungerThan40 = youngerThan40[youngerThan40.Sex == 'male'].Survived.value_counts()
figure4 = plt.figure(4)
plt.pie(malesYoungerThan40, autopct = '%0.1f%%', labels = ['Not survived','Survived'], explode = (0,0.05), colors = ['#FF4500','#00C0A3'])
plt.title('Male survivors younger than 40')
print(plt.show())

# ------------- Question 11 ---------------
# Showing the age with  20 bins
figure5 = plt.figure(5)
plt.hist(df.Age, bins = 20, color = 'aqua', edgecolor = 'orangered')
plt.title('Age distribution with 20 bins')
plt.xlabel('Age groups')
plt.ylabel('Nr. of passengers')
plt.xticks(np.arange(0,85,5))
print(plt.show())

# ------------- Question 12 ---------------
# Showing the age frequency of survived passengers
figure6 = plt.figure(6)
ageWithSurvived = df[df.Survived == 1].Age
plt.hist(ageWithSurvived)
plt.title('Age frequency of survived passengers')
plt.xlabel('Age groups')
plt.ylabel('Nr. of survivors')
print(plt.show())

# ------------- Question 13 ---------------
# Showing a survived males and females on a bar chart
# figure7 = plt.figure(7)
# survivedMales_Females = dict(df[df.Survived == 1].Sex.value_counts())
# xValues = survivedMales_Females.keys()
# yValues = survivedMales_Females.values()
# plt.bar(xValues, yValues)
# print(survivedMales_Females)
# print(plt.show())
# ============ TODO: Practise how to create bar chart with Matplotlib=============

# ------------- Question 13 ---------------
# Showing, in a bar chart, how many passengers survived in each class
# Showing Bar graph for Survived with male, female, class 
figure8 = plt.figure(8)
survivors = df[df.Survived == 1]
maleSurvivors = dict(survivors[survivors.Sex == 'male'].Pclass.value_counts())
maleSurvivors_X = maleSurvivors.keys()
maleSurvivors_Y = maleSurvivors.values() 
classes = []
for x in maleSurvivors_X:
    if x == 1:
        classes.append('first-class')
    elif x == 2:
        classes.append('second-class')
    elif x == 3:
        classes.append('third-class')
FemaleSurvivors = dict(survivors[survivors.Sex == 'female'].Pclass.value_counts())
FemaleSurvivors_X = FemaleSurvivors.keys()
FemaleSurvivors_Y = FemaleSurvivors.values() 
xpositions = np.arange(len(classes))
width = 0.25
plt.bar(xpositions - width/2, maleSurvivors_Y, width, label = 'Male survivors')
plt.bar(xpositions + width/2, FemaleSurvivors_Y, width , label = 'Female survivors')
plt.title('Survivors across different classes based on gender')
plt.xlabel('Classes')
plt.ylabel('Nr. of survivors')
plt.xticks(xpositions, classes)
plt.legend()
print(plt.show())

# ================ TODO: Customize to appropriately answer the question

# ------------- Question 14 ---------------
# Showing how many passengers travelled in different classes
figure9 = plt.figure(9)
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

# ------------- Question 15 ---------------
# Showing, in a bar chart, survivors across different classes
figure10 = plt.figure(10)
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

# ------------- Question 16 ---------------
# Showing Question-13 & Question-14 in subplot 
fig, axes = plt.subplots(1,2, figsize = (10,3))
figure11 = plt.figure(11)
# Showing Bar graph for Survived with male, female, class 
survivors = df[df.Survived == 1]
maleSurvivors = dict(survivors[survivors.Sex == 'male'].Pclass.value_counts())
maleSurvivors_X = maleSurvivors.keys()
maleSurvivors_Y = maleSurvivors.values() 
classes1 = []
for x in maleSurvivors_X:
    if x == 1:
        classes1.append('first-class')
    elif x == 2:
        classes1.append('second-class')
    elif x == 3:
        classes1.append('third-class')
        
FemaleSurvivors = dict(survivors[survivors.Sex == 'female'].Pclass.value_counts())
FemaleSurvivors_X = FemaleSurvivors.keys()
FemaleSurvivors_Y = FemaleSurvivors.values() 
xpositions = np.arange(len(classes1))
width = 0.25

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


axes[0].bar(xpositions - width/2, maleSurvivors_Y, width)
axes[0].bar(xpositions + width/2, FemaleSurvivors_Y, width)
axes[1].bar(classes, yValues)
print(plt.show())

# TODO: Find a way to customize the axis

#  ------------------ Question 17 ------------------

# Showing Bar graph for Survived with 3rd class male, 1st class female
figure12 = plt.figure(12)
firstClassFemaleSurvivors = df[(df.Pclass == 1) & (df.Survived == 1) & (df.Sex == 'female')]   #Getting first class female survivors
thirdClassMales = df[(df.Pclass == 3) & (df.Survived == 1) & (df.Sex == 'male')]   #Getting third class male survivors

dimByMeasure = {'females': len(firstClassFemaleSurvivors), 'males' : len(thirdClassMales)}   #a dictionary to use to plot the graph
xValues = dimByMeasure.keys()
yValues = dimByMeasure.values()

plt.bar(xValues, yValues)
plt.xlabel('Gender')
plt.ylabel('Nr. of Survivor')
plt.title('Survived males and females in 3rd and 1st class  respectively')
print(plt.show())
# =============== TDOD: Show the markers ===============

# --------------- Question 18 ---------------
# first class female passengers that survived / not survived 
figure13 = plt.figure(13)
firstClassFemales = df[(df.Sex == 'female') & (df.Pclass == 1)].Survived.value_counts()
plt.pie(firstClassFemales, autopct = '%0.1f%%', labels = ['Survived','Not survived'], colors =['#ff0000','#00C0A3'])
plt.title('First class female survived-vs-not survivors passengers')
print(plt.show())

# -------------- Question 19 ------------------
# Mapping the Sex column male = 1, female = 0 
sexColumn = dict(df.Sex)
# sexColumn.keys()
newSexColumn = []
for v in sexColumn.values():
    if v == 'female':
        newSexColumn.append(0)
    elif v == 'male':
        newSexColumn.append(1)

df['newSexColumn'] = newSexColumn   #Inserting the new sex column
print(df)

# ----------------- Question 20 ----------------
# Finding the NULL values
_passengerID = df[df.PassengerId.isnull()]    #For the PassengerId column
# _passengerID
_survived = df[df.Survived.isna()]    #For the Survived column
# _survived
_pClass = df[df.Pclass.isna()]    #For the Pclass column
# _pClass
_name = df[df.Name.isnull()]    #For the name column
# _name
_sex = df[df.Sex.isnull()]    #For the sex column
# _sex
_age = df[df.Age.isna()]    #For the age column
# _age
_sibSp = df[df.SibSp.isna()]    #For the SibSp column
# _sibSp
_parch = df[df.Parch.isnull()]    #For the parch column
# _parch
_ticket = df[df.Ticket.isnull()]    #For the ticket column
# _ticket
_fare = df[df.Fare.isnull()]    #For the Fare column
# _fare
_cabin = df[df.Cabin.isnull()]    #For the cabin column
# _cabin
_embarked = df[df.Embarked.isnull()]    #For the embarked column
# _embarked
_newSexColumn = df[df.newSexColumn.isnull()]    #For the newSexColumn column
# _newSexColumn

# --------------  Question 21 -----------------
#  Replacing Null values with a default value
df.Age.fillna(math.floor(df.Age.mean()))   #Setting default value for the NULLs in the Age column

df.Cabin.fillna('unknown', inplace = True)   #Setting default value for the NULLs in the Cabin column

# ---------------- Question 22 -----------------
# Dropping unwanted columns
newFrame = df.drop(columns = ['Ticket','Fare','Embarked','newSexColumn', 'SibSp','Cabin','Parch'])
print(newFrame)