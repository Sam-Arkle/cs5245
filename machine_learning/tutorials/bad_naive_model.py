# Don't do this, it is a bad approach.
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)

model.fit(X, y)
y_model = model.predict(X)

from sklearn.metrics import accuracy_score

print("Accuracy score is: ", accuracy_score(y, y_model))


# Our score will be 1.0. We have trained and evaluated our model on the same data. This is bad.

# So we want a holdout set of data which we don't train on.

from sklearn.model_selection import train_test_split
# Below splits the data with 50% in each set
X1, X2, y1, y2 = train_test_split(X, y, random_state=0, train_size=0.5)

model.fit(X1, y1)

y2_model = model.predict(X2)
print("The new accuracy score is: ", accuracy_score(y2, y2_model))


# Problem with witholding half our data is that we have less data to train our model on :(

# To solve this, we can use cross validation. Sequence of fits where each subset of the data is used both as a training set and as a validaiton set
# We could do that with the data before as such:
y2_model = model.fit(X1, y1).predict(X2)
y1_model = model.fit(X2, y2).predict(X1)
print("First accuracy score cross validation: ", accuracy_score(y1, y1_model))
print("Second accuracy score cross validation: ", accuracy_score(y2, y2_model))

# Above we have folded the data only twice. We can do it many times.
# There are convenience functions in sklearn to do this for us!

from sklearn.model_selection import cross_val_score
print("five folds using convenience method: ", cross_val_score(model, X, y, cv=5))

# We can take this to an extreme and have as many folds as data points: leave one out cross validation:

from sklearn.model_selection import LeaveOneOut
scores = cross_val_score(model, X, y, cv=LeaveOneOut())
print("Leave one out accuracy score: ", scores)
print("Average of above = ", scores.mean())

# "Check out other handy scheme online http://scikit-learn.org/stable/modules/cross_validation.html"