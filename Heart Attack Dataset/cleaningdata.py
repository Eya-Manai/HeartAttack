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



