import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# plt.rcParams['text.usetex'] = True
problem = 1
problem_name = f'challenge_{problem:02d}'
train_file = f'{problem_name}.npz'
data = np.load(train_file)
x_train = data['x_train']
y_train = data['y_train']
x_test = data['x_test']

plt.clf()
plt.scatter(x_train[y_train == 0, 0], x_train[y_train == 0, 1], label=r'$y=0$',
            color='blue', marker='*')
plt.scatter(x_train[y_train == 1, 0], x_train[y_train == 1, 1], label=r'$y=1$',
            color='red', marker='+')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title(f'Data set {problem} train')
plt.legend()
plt.axis('equal')
plt.show()

# Splitting up the test data
from sklearn.model_selection import train_test_split, LeaveOneOut

X_train, X_test, y_train_new, y_test = train_test_split(x_train, y_train, test_size=0.4, random_state=42)

# model is your classifier (any object with a fit and predict method)
# model = GaussianNB()


# model.fit(X_train, y_train_new)
#
# y_hat = model.predict(X_test)

# Trying it out with crosss validation:
# from sklearn.model_selection import cross_val_score
#
# scores = cross_val_score(model, x_train, y_train, cv=178)
# print(scores.mean())\
#     Using GNB the best we get is: 0.9438202247191011
# Trying to iterate through options for above
# maximum = (0, 0)
# for i in range(2, 200):
#     scores = cross_val_score(model, x_train, y_train, cv=i)
#     if maximum[0] < scores.mean():
#         maximum = (scores.mean(), i)

# print("The optimal fold number is: ", maximum[0], maximum[1])
# checking the accuracy of the model

from sklearn.metrics import accuracy_score
# print("Accuraccy score is: ", accuracy_score(y_test, y_hat))
# submission_file = f'{problem_name}_submission.npz'
# np.savez(submission_file, y_test=y_hat)

# Trying with svm:
clf = SVC(gamma=2, C=1)
clf.fit(X_train, y_train_new)
y_hat = clf.predict(X_test)
print("Accuracy score is: ", accuracy_score(y_test, y_hat))
# This gives a score of 0.88
# Need to try softening the margins as there is obviously overlap going on too


# Talk with Dr parry: Note, should be same number of folds to compare each model.

# We aren't submitting our models. We are just submitting the labels we have made and they will be compared against
# stuff on webcat. Or something to that effect. The actual models will be evaluated by Dr Parry.