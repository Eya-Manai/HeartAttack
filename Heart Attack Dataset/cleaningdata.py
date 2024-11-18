import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


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

#Heart Rate Max  Vs Age for Exercise Angina
figure1=plt.figure(figsize=(6,6))
sns.scatterplot(data=data,x='age', y='max heart rate',hue='exercise angina')
ax = sns.lineplot(data=data,x='age',y='max heart rate')
plt.title("Heart Rate Max  Vs Age for Exercise Angina")
plt.xlabel("Age")
plt.ylabel("Max Heart Rate")
plt.show()
####Distribution of Chest Pain Types by Exercising Status
figure2=plt.figure(figsize=(6,6))
sns.countplot(data=data,x='chest pain type',hue='exercise angina',palette='Set2')
plt.title('Distribution of Chest Pain Types by Exercising Status')
plt.xlabel("chest pain type")
chestP_Level=["Typical Angina","Atypical","Non anginial Pain","Asymptomatic"]
plt.xticks(ticks=[0,1,2,3],labels=chestP_Level)
plt.ylabel(" Count exercise angina")
plt.show()
####Distribution of Chest Pain Types by Sex Status
figure3=plt.figure(figsize=(6,4))
sns.countplot(data=data,x='chest pain type',hue='sex',palette='Set1')
plt.title('Distribution of Chest Pain Types by Sex Status')
plt.xticks(ticks=[0,1,2,3],labels=chestP_Level)
plt.ylabel(" Count people")
plt.show()
###Oldpeak vs Heart Rate, by Slope
figure3=plt.figure(figsize=(6,6))
sns.scatterplot(data=data,x='oldpeak', y='max heart rate',hue='ST slope')
plt.xlabel('Oldpeak (ST Depression)')
plt.ylabel('Heart Rate (Thalachh)')
plt.title('Oldpeak vs Heart Rate, by Slope')
plt.show()






