import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#filename = "data.csv"
filename = "CuboBase.csv"

# Assign colum names to the dataset
#names = ['age', 'income', 'student', 'credit_rating', 'Class:buys_computer']
names = ['realese_date', 'duration_ms', 'tempo', 'popularity' , 'key']

# Read dataset to pandas dataframe
dataset = pd.read_csv(filename, names=names)

print(dataset.head())

dataset['realese_date'] = dataset['realese_date'].str.replace('-','')

X = dataset.iloc[:, :-1].values.astype(int)
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
