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
data['cholesterol'] = data['cholesterol'].replace(0, np.nan)
data['cholesterol'] = data['cholesterol'].fillna(data['cholesterol'].median())
print("Missing in Data after cleaning :", data.isna().sum().sum())
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

####
figure4=plt.figure(figsize=(10,7))
ax = figure4.add_subplot(111, projection='3d')
sc = ax.scatter(data['oldpeak'], data['max heart rate'], data['ST slope'], c=data['ST slope'], cmap='viridis', s=60)
ax.set_xlabel('Oldpeak (ST Depression)')
ax.set_ylabel('Heart Rate (max heart rate)')
ax.set_zlabel('Slope (ST slope)')
plt.colorbar(sc, label='Slope (SLP)')
plt.title('Oldpeak vs Heart Rate vs Slope')
plt.show()
####
main_feature_col = [
    'age', 'sex', 'chest pain type', 'resting bp s', 
    'cholesterol', 'max heart rate', 'oldpeak', 
    'ST slope', 'exercise angina'
]

# Create the plot
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.flatten()

# Plot histograms
for i, col in enumerate(main_feature_col):
    try:
        # For numerical columns
        sns.histplot(data=data, x=col, hue='target', multiple='layer', ax=axes[i])
    except TypeError:
        # For categorical columns
        sns.countplot(data=data, x=col, hue='target', ax=axes[i])
    
    # Customize plot
    axes[i].set_title(f'{col} VS Heart Attack Risk')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Frequency')
    axes[i].legend(title='Heart Attack Risk', labels=['Low Risk', 'High Risk'])
plt.tight_layout()
plt.show()

# Alternative visualization for numerical features
numerical_features = [
    'age', 'resting bp s', 'cholesterol', 
    'max heart rate', 'oldpeak'
]

fig, axes = plt.subplots(2, 3, figsize=(5, 5))
axes = axes.flatten()

for i, col in enumerate(numerical_features):
    sns.boxplot(data=data, x='target', y=col, ax=axes[i])
    
    # Customize plot
    axes[i].set_title(f'{col} Distribution by Heart Attack Risk')
    axes[i].set_xlabel('Heart Attack Risk')
    axes[i].set_ylabel(col)
    axes[i].set_xticklabels(['Low Risk', 'High Risk'])

plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 10))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Features')
plt.tight_layout()
plt.show()






