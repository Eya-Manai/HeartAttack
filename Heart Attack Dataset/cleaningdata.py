import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\HeartCatalogue.csv')
data.rename(columns={"Output:": "HeartAttackRisk"}, inplace=True)
print(data.head())
print(data.info)
print(data.columns)
print("Missing in Data :" , data.isna().sum().sum())
print("Duplicated in Data :" , data.duplicated().sum())
data.drop_duplicates(inplace=True)
print("Duplicated in Data :" , data.duplicated().sum())
#print(data[data.duplicated()])
figure1=plt.figure(figsize=(6,6))
sns.scatterplot(data=data,x='age', y='max heart rate',hue='exercise angina')
ax = sns.lineplot(data=data,x='age',y='max heart rate')
plt.title("Heart Rate Max  Vs Age for Exercise Angina")
plt.xlabel("Age")
plt.ylabel("Max Heart Rate")
plt.show()
figure2=plt.figure(figsize=(6,6))
sns.countplot(data=data,x='chest pain type',hue='exercise angina',palette='Set2')
plt.title('Distribution of Chest Pain Types by Exercising Status')
plt.xlabel("chest pain type")
chestP_Level=["Typical Angina","Atypical","Non anginial Pain","Asymptomatic"]
plt.xticks(ticks=[0,1,2,3],labels=chestP_Level)
plt.ylabel(" Count exercise angina")
plt.show()





