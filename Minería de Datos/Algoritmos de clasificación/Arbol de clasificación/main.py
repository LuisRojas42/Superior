import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#datos = pd.read_csv("data2.csv", delimiter=",")
#datos.drop('name',axis='columns', inplace=True)
datos = pd.read_csv("/Users/luisrojas/Downloads/Mineria de Datos/Algoritmo ID3/ID3_From_Scratch-main/data.csv", delimiter=",")
datos[0:5]
print("Datos:\n",datos)

buys_comp = datos['Class:buys_computer'].value_counts()
#buys_comp = datos['loan_decision'].value_counts()
print("Usr del target:\n",buys_comp)

x = datos[['age','income', 'student','credit_rating']].values
#x = datos[['age','income','loan_decision']].values
x[0:5]
print("Características originales:\n",x)

from sklearn import preprocessing
age = preprocessing.LabelEncoder()
age.fit(['youth','middle aged','senior'])
#age.fit(['youth','middle_aged','senior'])
x[:,0] = age.transform(x[:,0])

income = preprocessing.LabelEncoder()
income.fit(['high','medium','low'])
x[:,1] = income.transform(x[:,1])

student = preprocessing.LabelEncoder()
student.fit(['no','yes'])
x[:,2] = student.transform(x[:,2])

credit_rating = preprocessing.LabelEncoder()
credit_rating.fit(['fair','excellent'])
x[:,3] = credit_rating.transform(x[:,3])

x[0:5]
print("Características transformadas:\n",x)

y = datos['Class:buys_computer']
y[0:5]
print("Class:buys_computer: ",y)

from sklearn.model_selection import train_test_split
x_entre, x_test, y_entre, y_test = train_test_split(x, y, test_size=0.3, random_state=3)

print("Cantidad de datos para Tren de entreno: ",x_entre.shape, y_entre.shape)
print("Cantidad de datos para Tren de Testeo: ",x_test.shape, y_test.shape)

arbol = DecisionTreeClassifier(criterion="entropy", max_depth=2)

arbol.fit(x_entre,y_entre)

arbolpred = arbol.predict(x_test)

print('Prediccion del modelo: ',arbolpred [0:5])
print('Valores reales:\n',y_test [0:5])

from sklearn import metrics
import matplotlib.pyplot as plt
print('Precisión del árbol de decisiones: ',metrics.accuracy_score(y_test,arbolpred))

'''
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(arbol, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
fig.savefig("decistion_tree.png")
'''

'''
from sklearn.datasets import load_iris
from sklearn import tree

from sklearn.tree import export_text

iris = load_iris()
featurenames = datos.columns[0:4]
r = export_text(arbol)
print(r)
'''

from io import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree

dot_data = StringIO()
filename = "arbol_test.png"
featurenames = datos.columns[0:4]
targetNames = datos["Class:buys_computer"].unique().tolist()
out = tree.export_graphviz(arbol,feature_names=featurenames, out_file=dot_data, class_names = pd.unique(y_entre), filled=True) 
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100,200))
plt.imshow(img, interpolation='nearest')
