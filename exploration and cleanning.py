import pandas as pd

# Replace 'Win10' with your actual username
username = 'Win10'
file_path = r'C:\Users\{}\Downloads\titanic.csv'.format(username)

titanic = pd.read_csv(file_path)
print(titanic.shape)
print(titanic.info())
print(titanic.head(5))
print(titanic.describe())
categorical = titanic.dtypes[titanic.dtypes == "object"].index
print(categorical)
print(titanic[categorical].describe())
titanic.to_csv("titanic_new.csv", index=False)
import openpyxl
titanic.to_excel("titanic_new.xlsx", index=False)
ages = titanic["Age"]
print(ages.head())
# VARIABLE DESCRIPTIONS:
# survival        Survival
#                 (0 = No; 1 = Yes)
# pclass          Passenger Class
#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
# name            Name
# sex             Sex
# age             Age
# sibsp           Number of Siblings/Spouses Aboard
# parch           Number of Parents/Children Aboard
# ticket          Ticket Number
# fare            Passenger Fare
# cabin           Cabin
# embarked        Port of Embarkation
#                 (C = Cherbourg; Q = Queenstown; S = Southampton)
del titanic["PassengerId"] 
'''Survived" indicates whether each passenger lived or died. Since predicting survival is our goal, we definitely need to keep it.

Features that describe passengers numerically or group them into a few broad categories could be useful for predicting survival. The variables Pclass, Sex, Age, SibSp, Parch, Fare and Embarked appear to fit this description, so let's keep all of them.

We have 3 more features to consider: Name, Ticket and Cabin.

"Name" appears to be a character string of the name of each passenger. Let's look at name a little closer:'''
print(type(titanic["Age"]))
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(titanic["Cabin"][0:15])  
'''selection of column'''
print(titanic) 
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head())