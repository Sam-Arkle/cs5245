# We will use a generative model known as Gaussian naive Bayes.
# Assumes each class is drawn from an axis aligned Gaussian distribution.
# Often a good baseline classification as it is fast and has no hyperparams
# We will split data into training set and testing set

from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris = sns.load_dataset('iris')
X_iris = iris.drop('species', axis=1)
y_iris = iris['species']

Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)

print("accuracy is: ",  accuracy_score(ytest, y_model))